import requests
import json
import base64
from django.http import JsonResponse
from datetime import datetime
from . import settings
from .generateAccessToken import get_access_token

def initiate_stk_push(request):
    access_token_response = get_access_token(request)
    if isinstance(access_token_response, JsonResponse):
        access_token_data = json.loads(access_token_response.content.decode('utf-8'))
        access_token = access_token_data.get('access_token')

        if access_token:
            amount = 1
            phone = '254797245933'  # Ensure it's a string starting with '254'
            passkey = settings.MPESA_PASSKEY
            business_short_code = settings.BUSSINESS_SHORTCODE
            process_request_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
            callback_url = 'https://dad5-102-219-210-106.ngrok-free.app/stk/'
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password = base64.b64encode((business_short_code + passkey + timestamp).encode()).decode()
            party_a = '254708374149'  # Ensure it's a string starting with '254'
            party_b = business_short_code  # Should be integer
            account_reference = 'KIBARU'
            transaction_desc = 'Holds Funds'
            stk_push_headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            }

            payload = {
                "BusinessShortCode": int(business_short_code),
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": 'CustomerPayBillOnline',
                "Amount": amount,
                "PartyA": party_a,
                "PartyB": int(party_b),
                "PhoneNumber": phone,
                "CallBackURL": callback_url,
                "AccountReference": account_reference,
                "TransactionDesc": transaction_desc
            }

            try:
                response = requests.post(process_request_url, headers=stk_push_headers, json=payload)
                response.raise_for_status()
                response_data = response.json()
                checkout_response_id = response_data.get('CheckoutRequestID', None)
                response_code = response_data.get('ResponseCode', '-1')

                if response_code == '0' and checkout_response_id:
                    return JsonResponse({'CheckOutResponseID': checkout_response_id, 'ResponseCode': response_code})
                else:
                    return JsonResponse({'error': 'Failed to initiate STK push'})

            except requests.exceptions.RequestException as e:
                return JsonResponse({'request error': str(e)})
            
        else:
            return JsonResponse({'error': 'Access token not found'})

    else:
        return JsonResponse({'error': 'Failed to retrieve access token'})

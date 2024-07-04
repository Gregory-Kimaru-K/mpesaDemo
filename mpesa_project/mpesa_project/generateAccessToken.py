import requests
from django.http import JsonResponse
from mpesa_project import settings

def get_access_token(request):
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    headers = {'Content-Type' : 'application/json'}
    auth = (consumer_key, consumer_secret)
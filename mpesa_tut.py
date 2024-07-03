import requests
from requests.auth import HTTPBasicAuth

consumer_key = 'c54l71UFtdhQtcIaOu6AmNh07GGJA04I8XE0X6fIINtx1zIw'
consumer_sec = '0u9hwd8UQW22JRrb64rFUxW1Qt1UvKlQvHNDiodO71BG0ls4JZO0NksJOxAgssyA'

api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

response = requests.get(api_url, HTTPBasicAuth(consumer_key, consumer_sec))

print(response.json())

if response.status_code == 200:
    access_token = reponse.json().get('access_token')
    if access_token:
        print(f'Access Token : {access_token}')

    else:
        print("Cannot find access token")

else:
    print(f'Failed Status code:{response.status_code}')
    print(f'Error : {response.json()}')

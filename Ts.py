import requests

number = "01091565831"
password = "Mm86700@@"
url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "x-dynatrace": "MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem": "1630483957",
    "clientId": "AnaVodafoneAndroid",
    "x-agent-device": "RMX1911",
    "x-agent-version": "2021.12.2",
    "x-agent-build": "493",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "143",
    "Host": "mobile.vodafone.com.eg",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.1",
}

data = {
    "username": number,
    "password": password,
    "grant_type": "password",
    "client_secret": "a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",
    "client_id": "my-vodafone-app",
}

try:
    response = requests.post(url, headers=headers, data=data, verify=False)
    response.raise_for_status()
    jwt = response.json()["access_token"]
    print("Access token:", jwt)
except requests.exceptions.RequestException as e:
    print("An error occurred:", str(e))

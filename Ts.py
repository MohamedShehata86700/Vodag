import requests
import time
import asyncio
import requests
import requests
import random
import time

#################### Colour ##############
F = '\033[1;32m' #اخضر
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
PN='\033[1;35m' #BINK
print(random.choice([F, B, R, G, Y, Bl, P, C, W, PN]) +f"""


88      a8P   88                            
88    ,88'    ""                            
88  ,88"                                    
88,d88'       88  8b,dPPYba,    ,adPPYb,d8  
8888"88,      88  88P'   `"8a  a8"    `Y88  
88P   Y8b     88  88       88  8b       88  
88     "88,   88  88       88  "8a,   ,d88  
88       Y8b  88  88       88   `"YbbdP"Y8  
                                aa,    ,88  
                                 "Y8bbdP"   
==============================          
{R}<WELCOM IN Voda CARD BY MOHAMEED SHEHATA> 
<King Of Deebweb>>@Mohamed86
==============================     
""")

number="01277943538"
#print("$"*10)
password="Mm86700@@"
#print("$"*10)
url="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headers={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
data={
"username":number,

"password":password,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
res=requests.post(url, headers=headers, data=data)

#print(res)

jwt=res.json()["access_token"]


#print("=" * 40)

#print(jwt)

def cart():

	ul=f"https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type=RamadanHub&channel=website&msisdn={number}"
	
	
	hd={
	          "Host": "web.vodafone.com.eg",
	          "Connection": "keep-alive",
	          "msisdn": number,
	          "api-host": "PromotionHost",
	          "Accept-Language": "AR",
	          "Authorization": "Bearer "+(jwt)+"",
	          'Content-Type': 'application/json',
	          'x-dtreferer': 'https://web.vodafone.com.eg/spa/portal/hub',
	          'Accept': 'application/json',
	          'clientId': 'WebsiteConsumer',
	          'User-Agent': 'Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36',
	          'channel': 'WEB',
	          'Referer': 'https://web.vodafone.com.eg/spa/portal/hub',
	          'Accept-Encoding': 'gzip, deflate, br'
	                    }
	                    
	                    
	                    
	                    
	                    
	r =requests.get(ul, headers=hd).json()
	for i in r:
		try:
		   patt=i['pattern']
		   #print(patt)
		   for a in patt:
		   	action=a['action']
		   	#print(action)
		   	for zxc in action:
		   		ch=zxc['characteristics']
		   		#print(ch)
		   		ncharge=(ch[0]['value'])
		   		vcharge=(ch[1]['value'])
		   		cnum=(ch[3]['value'])
		   		#print(f"{R}  -_-  "*10)
		   		print(f'{Y}charge Number Available is >> {G}{ncharge}')
		   		print(f'{Y}Card Value is >> {G}{vcharge} unit')
		   		print(f'{Y}Your Card is >> {G}{cnum}')
		   		print(f"{R}  -_-  "*9)
		   		
		   		
		   		
		   		

		   
		except:
 	   	  pass
while True:	   
    cart()

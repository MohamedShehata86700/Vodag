
import requests
import telebot
from telebot import types
token= "6550384531:AAFoPmjpJKHIUYcSH9P6ycKa7mSq2UikR_U"
bot = telebot.TeleBot(token)
owner=836970770
id1="-1001704325012"



number="01091565831"
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
jwt=res.json()["access_token"]

printed_values = []
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
		   		if float(vcharge) > 200:
		   			if vcharge not in printed_values:
		   				printed_values.append(vcharge)	
		   		
				   		#print(f"{R}  -_-  "*10)
				   		z=f"𖡋    »  »  » كرت {vcharge} وحده 🌙❤️\n `*858*{cnum}#` \n{ncharge} شحنه اضغط للنسخ 🔥‼️\nحط تفاعل ننزل بالكارت التاني ❤️‍🔥\n𖡋    »    سبحان الله وبحمده\n𖡋    »   سبحان الله العظيم"

				   		bot.send_message(id1,text=z,parse_mode="markdown")
		except:
 	   	  pass
while True:
	try:	   
		cart()
	except:pass		

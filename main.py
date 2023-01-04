import telebot,requests,time,os,random
token = "5204198818:AAFYGV2CC_w11-Y0w8nbKwriac6RSPA92BY"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hello {message.from_user.first_name},\n=== === ===\nWellcome Back Sir...!❤️\n</strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def ps(message):
	msg=message.text
	x = int(msg)
	while True:
		x = x + 1
		number = "01559773184"
		url = "https://api-my.te.eg/api/user/generatetoken?channelId=WEB_APP"
		hd = { 'Host' :  'api-my.te.eg' ,'Connection' :  'keep-alive' ,'Accept' :  'application/json, text/plain, */* ','User-Agent' :  'Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 ','Origin' :  'https://my.te.eg' , 'Referer' :  'https://my.te.eg/' ,'Accept-Encoding' :  'gzip, deflate, br' ,'Accept-Language' :  'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7' }
		re = requests.get(url,headers=hd).json()
		jwt = re["body"]["jwt"]
		url2 = "https://api-my.te.eg/api/user/login?channelId=WEB_APP"
		hd2 = {'Jwt':jwt,'Content-Type':"application/json; charset=utf-8","User-Agent":"okhttp/3.12.1","Host":"api-my.te.eg","Connection":"Keep-Alive","Accept-Encoding":"gzip","Content-Length":"159"}
		data = '{"header":{"msisdn":"%s","timestamp":"1666168987","locale":"en"},"body":{"password":"HXgtyLkYSc1f+m0kqmYW/w=="}}' %(number)
		r = requests.post(url2,headers=hd2,data=data).json()
		responseMessage=r['header']['responseMessage']
		customerId=r['header']['customerId']
		referenceId=r['header']['referenceId']
		channelId=r['header']['channelId']
		if "Login successful" in responseMessage:
			jwt2 = r['body']['jwt']
			url3 = "https://api-my.te.eg/api/services/change/mainoffers"
			hd3= {'Jwt':jwt2,'Content-Type':"application/json; charset=utf-8","User-Agent":"okhttp/3.12.1","Host":"api-my.te.eg","Connection":"Keep-Alive","Accept-Encoding":"gzip","Content-Length":"159"}
			data2 = {"header":{"customerId":customerId,"msisdn":number,"locale":"ar","messageCode":"CHANGE_MAIN_PLAN"},"body":{"offerId":x,"parentOfferId":"1000"}}
			r3 = requests.post(url3,headers=hd3,json=data2).json()
			responseMessage2=r3['header']['responseMessage']
			bot.send_message(message.chat.id,f"<strong>Done Login\nID:{x}\nResponsed:{responseMessage2}</strong>",parse_mode="html")
		else:
			bot.send_message(message.chat.id,f"<strong>Error Login</strong>",parse_mode="html")
bot.polling()

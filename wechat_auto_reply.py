import itchat
import requests

#login wechat
#itchat.login()
itchat.auto_login(hotReload=True)
apicUrl = 'http://www.tuling123.com/openapi/api'
def get_info(message):
	data = {
		'key':'6a6f71a5535b4abea1c2207615097eb8',
		'info': message,
		'userid':'robot'
	}
	try:
		response_json = requests.post(apicUrl, data=data).json()
		info = response_json['text']
		return info;
	except Exception as e:
		return

#get the wechat message from friend
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
	#default_reply = 'I get it'
	#friend = itchat.search_friends(name = 'Katherineિ🎅🏻ી')
	#rf = friend[0]['UserName']
	reply = get_info(msg['Text'])
	#if(msg['FromUserName'] == rf):
		itchat.send(reply, toUserName=rf)
#response the wechat message from friend
itchat.run()

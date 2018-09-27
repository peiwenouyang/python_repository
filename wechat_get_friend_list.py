import itchat

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()[0:]

for i in friends[1:]:
	print(i)
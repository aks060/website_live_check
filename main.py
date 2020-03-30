#/usr/bin/python3
import os
import requests
import time

s=requests.session()
sites=open('sitelist.txt')
while 1:
	for i in sites:
		print('running for '+i)
		try:
			res=s.get(i.strip())
			if res.status_code!=200:
				os.system('espeak "'+i+" is down. Please check it'")
				os.system('notify-send -t 10000 "'+i+' down." "'+i+' is down please check it"')
				os.system('termux-tts-speak "'+i+' is down"')
		except:
			os.system('espeak "'+i+' is down. Please check it"')
			os.system('notify-send -t 10000 "'+i+' down." "'+i+' is down please check it"')
			os.system('termux-tts-speak "'+i+' is down"')
	time.sleep(60)
import requests
import sys
import os
import signal

signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))

url = sys.argv[1]

arq = open(sys.argv[2],'r')
lines = arq.readlines()
arq.close

for line in lines:
	line = line.replace("\n", "")
	request = url+"/"+line
	http = requests.get(request)
	code = http.status_code
	if code != 301 and code != 404:
		if not "Page not found" in http.content:
			print("[+] PAGE FOUND: "+request)
		else:
			print("[-] PAGE NOTFOUND: "+request)
	else:
		print("[-] PAGE NOTFOUND: "+request)

print("FINISH!!! <3")
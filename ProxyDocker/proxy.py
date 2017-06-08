#!usr/bin/env python

import threading
from socket import *


def do_this(dicti):
	server_sd = socket()
	host = gethostbyname("server") 
	print("Server socket created\n")
	port = dicti['port']
	server_sd.connect((host, port))
	print("Server socket connected\n")
	client_sd = dicti['client_sd']
	while True:
		message = client_sd.recv(1024)
		if len(message) == 0: 
			break
		print 'Message from client: %s\n' % message
		server_sd.send(message)
		message = server_sd.recv(1024)
		if len(message) == 0:
			break
		print 'Message to client: %s\n' % message
		client_sd.send(message)
	
	
	
	
def main():
	port = 7896 #server port
	host = gethostname()
	proxy_port = 9654 #proxy port
	
	ip = gethostbyname(gethostname())
	
	print ("This is the Server's ip address \n", ip)
	
	proxy_sd = socket()
	print ("Proxy created\n")
	
	proxy_sd.bind((host, proxy_port))
	proxy_sd.listen(3)
	while True:
		client_sd, addr = proxy_sd.accept()
		print("Client with socket-desc = ", client_sd, " got connected\n")
		if (client_sd>0):
			dicti = dict()
			dicti['client_sd'] = client_sd
			dicti['ip'] = ip
			dicti['port'] = port
			my_thread = threading.Thread(target=do_this, args=(dicti, ))
			my_thread.start()
	
	
	
if(__name__ == "__main__"):
	main()

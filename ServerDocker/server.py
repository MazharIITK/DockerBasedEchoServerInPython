#!usr/bin/python

from socket import *
import thread

#thread function
def thread_server(threadName, dup_sd):
	print dup_sd
	while True:
		message = dup_sd.recv(1024)
		print("Message from ", threadName, "is", message)
		dup_sd.send(message)
	dup_sd.close()
	
	

s = socket() 
host = gethostname()

server_port = 7896

s.bind((host, server_port))

while True:
	s.listen(3)
	dup_sd, addr = s.accept()
	thread.start_new_thread(thread_server, ("Thread_server", dup_sd, ) )
dup_sd.close()

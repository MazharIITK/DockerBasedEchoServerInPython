#!/usr/bin/python

from socket import *

s = socket()
host = gethostname()
port = input("Enter the port of the proxy: ")

print host

s.connect((host, port))

while True: 
    message_to_server = raw_input("Message to server: ")

    s.send(message_to_server)
    
    print 'Message from server: %s\n' % (s.recv(1024))
s.close

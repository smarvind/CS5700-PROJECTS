PREVIOUS CODE:

import socket
import re

host = '127.0.0.1'
port = 5123

sock = socket.socket()
sock.connect((host,port))
user = “cs5700spring2016 HELLO 001795233\n”
sock.send(user)
num = 0
while num != 'BYE':
	data3 = sock.recv(4096)
	num = str(data3)
	print num
	num1 = re.findall(r'\d', num)

	num2 = re.findall(r'[\+\-\*\/{B}]', num)

	if num2[0] == '+':
		num3 = str(int(num1[0]) + int(num1[1]))
		sock.send(num3)
		print "The message is sent to the server"	
	elif num2[0] == '-':
		num3 = str(int(num1[0]) - int(num1[1]))
		print "The message is sent to the server"
	elif num2[0] == '*':
		num3 = str(int(num1[0]) * int(num1[1]))
		print "The message is sent to the server"
	elif num2[0] == '/': 
		num3 = str(int(num1[0]) / int(num1[1]))
		print "The message is sent to the server"
	else:
		print num
		sock.close()
		#break
	#data = sock.recv(4096)
	#print "message recieved from server"
	#print data
#sock.close()
















CURRENTLY COMPLETE CODE:

import socket
import re

host = 'cs5700sp16.ccs.neu.edu'
port = 27993

sock = socket.socket()
sock.connect((host,port))

user1 = 'cs5700spring2016 HELLO 001795233\n'
sock.send(user1)

num = 0
while True:
        data3 = sock.recv(4096)
        num = str(data3)
        print num
        num1 = re.split(r'\s', num)
        num2 = re.findall(r'[\+\-\*\/{B}]', num)
        print num1
        print num2
        if num2[0] == '+':
                num3 = str(int(num1[2]) + int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                sock.send(num4)
                print num2
                print num4
        elif num2[0] == '-':
                num3 = str(int(num1[2]) - int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                sock.send(num4)
                print num3
                print num4
        elif num2[0] == '*':
                num3 = str(int(num1[2]) * int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                sock.send(num4)
                print num3
                print num4
        elif num2[0] == '/':
                num3 = str(int(num1[2]) / int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                sock.send(num4)
                print num3
                print num4
        else:
                print "connection terminated"
                break
sock.close()








CURRENTLY COMPLETE CODE WITH SSL:27994

import socket
import ssl
import re

from ssl import wrap_socket, CERT_NONE, PROTOCOL_TLSv1, SSLError
from ssl import SSLContext

host = 'cs5700sp16.ccs.neu.edu'
port = 27994

sock = socket.socket()
sock.connect((host,port))

ssl_socket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, server_hostname = host)

user1 = 'cs5700spring2016 HELLO 001795233\n'
ssl_socket.send(user1)

num = 0
while True:
        data3 = sock.recv(4096)
        num = str(data3)
        print num
        num1 = re.split(r'\s', num)
        num2 = re.findall(r'[\+\-\*\/{B}]', num)
        print num1
        print num2
        if num2[0] == '+':
                num3 = str(int(num1[2]) + int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                ssl_socket.send(num4)
                print num2
                print num4
        elif num2[0] == '-':
                num3 = str(int(num1[2]) - int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                ssl_socket.send(num4)
                print num3
                print num4
        elif num2[0] == '*':
                num3 = str(int(num1[2]) * int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                ssl_socket.send(num4)
                print num3
                print num4
        elif num2[0] == '/':
                num3 = str(int(num1[2]) / int(num1[4]))
                num4 = 'cs5700spring2016 ' + num3 + '\n'
                ssl_socket.send(num4)
                print num3
                print num4
        else:
                print "connection terminated"
                break
ssl_socket.close()

SCRIPT:




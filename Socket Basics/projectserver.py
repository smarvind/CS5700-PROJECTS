import socket

host = "127.0.0.1"
port = 5123

sock = socket.socket()
sock.bind((host,port))
sock.listen(5)
conn, addr = sock.accept()
while True:
	data2 = raw_input()
	conn.send(data2)
	print data2
	data = conn.recv(4096)
	print data
	print 'message recieved from client'
	
conn.close()	
	

num4 = ‘cs5700spring2016’ + num3 + ‘\n’
sock.send(num4)


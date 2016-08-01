import socket
import re
import urllib
import os
import sys
import webbrowser

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8',0))                                # Determining Src Ip us$
IP = s.getsockname()[0]
print IP
cachepath = os.popen('pwd').readlines()
cachepath1 = cachepath[0]
print cachepath1 

host = IP
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)


while True:
        clients, caddr = s.accept()
        print "Connection from: " + 'caddr'
        req = clients.recv(1024)
        print req
        #[/\w:?]*
        match1 = re.match(r'(GET /\sHTTP/1)', req)
        search = re.findall(r'GET ([/\w:?]*)', req)
        print search[0]
        #match2 = re.match('GET [/\w:?]*\sHTTP/1', req)
        #match3 = re.find
        #print match1.group()
        a = str(search[0])
        print a
        #print match2.group()
        if search:
             print "11111111111111111111111"
             #angle = match.group(1)
             #print "ANGLE: " + angle + "\n"
             url = "http://ec2-54-88-98-7.compute-1.amazonaws.com:8080" + a
             print url
             # [\w]*$
             #search1 = re.findall(r'[\w]*$', url)
	     search1 = url.split('/')
             print "search1"
             print search1
             print search1[-1]
             search_file = '/home/smarvind/c'
             if os.path.isfile(search_file):
                 print "if condition"
                 send_file = 'file:///' + search_file
                 clients.sendall(send_file)
             else:
                print "else condition"
                html = urllib.urlopen(url).read()
                #webbrowser.open(url)
                clients.sendall(html)
                f = open(search1[-1], "w")
                f.write(html)

        else:
                print"Return 404"
                clients.sendall("404 Not found\r\n")

        clients.close()




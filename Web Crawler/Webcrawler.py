#!usr/bin/python
import socket                                                                                           #Importing Necessary Modules
import sys
import re
import time
#---------------------------------------------------------------------SOCKET PROGRAMMING----------------------------------------------------------------------------------
host = 'cs5700sp16.ccs.neu.edu'                                                                         #Host
port = 80                                                                                               #Portnumber
username = sys.argv[1]                                                                                  #Username
password = sys.argv[2]                                                                                  #Password
s = socket.socket()
s.connect((host,port))                                                                                  #First Fakebook page
i1 = "Connection: keep-alive\r\n"
i2 = "Accept: text/html, application/xhtml+xml ,application/xml;q=0.9, image/webp,*/*;q=0.8\r\n"
i3 = "User-Agent: Mozilla/5.0 (windows NT 6.3; WOW64) \r\n"
i4 = "Accept-Language: en-US.en;q=0.8\r\n"
user = "GET / HTTP/1.1\r\nHost: cs5700sp16.ccs.neu.edu\r\nConnection: keep-alive\r\n"+i2+i3+i4+"\r\n"
s.send(user)
data1 = s.recv(4096)

def GET(data):                                                                                          #Function with a new socket to get the other pages of Fakebook
        s = socket.socket()
        s.connect((host, port))
        d1 = "GET /"+data+"/ HTTP/1.1\r\n"
        d2 = "Host: cs5700sp16.ccs.neu.edu\r\n"
        d3 = "Connection: keep-alive\r\n"
        d4 = "Accept: text/html, application/xhtml+xml ,application/xml;q=0.9, image/webp,*/*;q=0.8\r\n"
        d5 = "User-Agent: Mozilla/5.0 (windows NT 6.3; WOW64) \r\n"
        d6 = "Accept-Language: en-US.en;q=0.8\r\n\r\n"

        get_msg = d1+d2+d3+d4+d5+d6
        s.send(get_msg)
        response = s.recv(4096)
        s.close()
        return response
page2 = GET("fakebook")
data3 = GET("accounts/login/?next=/fakebook")

time.sleep(3)                                                                                           #Wait for 3 seconds
cookie = re.findall(r'csrftoken=(\w+)', data3, re.I)                                                    #Generate Cookie

session = re.findall(r'sessionid=(\w+)', data3, re.I)                                                   #Generate session id

a1 = "POST /accounts/login/ HTTP/1.1\r\n"                                                               #Sending POST Message
a2 = "Host: cs5700sp16.ccs.neu.edu\r\n"
a4 = "Accept: text/html ,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
a8 = "Cookie: csrftoken="+cookie[0]+"; sessionid="+session[0]+"\r\n"
a9 = "Connection: keep-alive\r\n"
a11 = "Cache-Control: max-age=0\r\n"
a13 = "Content-Length: 109\r\n"
a14 = "Origin: http://cs5700sp16.ccs.neu.edu\r\n"
a12 = "username="+username+"&password="+password+"&csrfmiddlewaretoken="+cookie[0]+"&next=%2Ffakebook%2F"
page4 = a1+a2+a9+a13+a11+a4+a14+a8+"\r\n"+a12
g = socket.socket()                                                                                     #Socket opening for persistent connections
g.connect((host,port))
g.send(page4)
time.sleep(5)
data4 = g.recv(4096)

session2 = re.findall(r'sessionid=(\w+)', data4, re.I)

user5 = "GET /fakebook/ HTTP/1.1\r\nHost: cs5700sp16.ccs.neu.edu\r\nConnection: keep-alive\r\nAccept: text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nCookie: csrftoken="+cookie$
g.send(user5)
data5 = g.recv(4096)
#------------------------------------------------------------------------WEBCRAWLER ALGORITHM-----------------------------------------------------------------------------
visited_links = []                                                                                      #Necessary Lists
unvisited_links = []
SECRET =[]


def extract_links(data):            
        find_links = re.findall('<a href="/fakebook/?\'?([^"\'>]*)', data)
        for links in find_links:
                if links not in unvisited_links :
                        unvisited_links.append(links)
        return unvisited_links

def send_links(data):                                                                                   #GET the links
        for links in unvisited_links:
                s3 = socket.socket()
                s3.connect((host, port))
                msg = "GET "+"/fakebook/"+links+" HTTP/1.1\r\nHost: cs5700sp16.ccs.neu.edu\r\nConnection: keep-alive\r\nAccept: text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n$
                s3.send(msg)
                data99 = s3.recv(4096)
                secret_FLAG2(data99)
                while len(secret) == 5:
                        s.close()
                        break
                links = extract_links(data99)
                s3.close()
global secret
def secret_FLAG2(data):                                                                                 #Traverse the pages to find the FLAGs
        global secret
        secret = re.findall(r'FLAG: (\w*)', data, re.I)
        #for i in secret:                                                                               #If the FLAGS are needed to be printed out as soon as the occur
        if secret != []:
        #               print i
                SECRET.append(secret)
        while len(SECRET) == 5:                                                                         #All the FLAGs will be generated at once
                print SECRET[0][0]
                print SECRET[1][0]
                print SECRET[2][0]
                print SECRET[3][0]
                print SECRET[4][0]
                s.close()
                exit()
                break
try:                                                                                                    #Calling the functions
        data98 = extract_links(data5)

        while unvisited_links != []:
                for links in unvisited_links:
                        send_links(links)
                        visited_links.append(links)
except KeyboardInterrupt:
        print "Was still Traversing :("
except ValueError:
        print "Value error occured"
except TypeError:
        print "Type of data mismatched"
except IndexError:
        print "Index error has occcured"

s.close()                                                                                               #Closing the socket
g.close()
exit()



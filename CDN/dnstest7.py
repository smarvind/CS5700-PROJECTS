import socket
import struct
import random
import sys


try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',0))
        IP = s.getsockname()[0]
	#print IP
except socket.error , er:
        print "ERROR SOCKET :", er[1]
        sys.exit()

host = IP
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
#s.listen(1)
class Packet_form:
	def __init__(self):
		self.id1 = 0
		self.flags = 0
		self.questcount = 0
		self.answerrec = 0
		self.NSrec = 0x0000
		self.addrec = 0x0000
		#self.DNSquery = query()
		#self.DNSanswer = answer()
		self.qname = ''
		self.qtype = 0
		self.qclass = 0
		self.qp = (())
		#print "constructor"
		#print type(self.qp)
	def create_header(self, id1, flags, questcount, answerrec, NSrec , addrec):
		header1 = struct.pack('!HHHHHH', id1, flags, questcount, answerrec, NSrec, addrec)
		return header1
	def create_query(self, q_name, q_type, q_class):

		query1 = struct.pack('!HHH', q_name, q_type, q_class)
		return query1

	def query_unpack(self):
		print "DNS server has started"
		#print "2"
		#packetquery = Sockets()
		#print "2.1"
		qpacket1=s.recvfrom(65535)
		#print "qpacket1"
            	#print qpacket1[0]
                #a=qpacket1
                #print a
                #sys.exit()
		qpacket = qpacket1[0].strip()
		global qp, id1
		qp = qpacket1[1]
		#print type(qp)
		[self.id, self.flags, self.questcount, self.answerrec, self.NSrec, self.addrec]= struct.unpack('!HHHHHH',qpacket[:12])
		#[self.id, self.flags, self.questcount, self.qname, self.qtype, self.qclass] = struct.unpack (!HHHHHH, qpacket [:12])
		id1 = self.id
		#print self.id #= qpacket[-32:-30]
		#print self.flags #= qpacket[-30:-28]
		#print self.questcount #= qpacket[-20:-4]
		#print self.answerrec #= qpacket[-4:-2]
		global query_data
		query_data=qpacket[12:]
		[self.qtype,self.qclass]= struct.unpack('!HH', query_data[-4:])
		#print "query"
		i = 0
		while True:
    			b = struct.unpack('!B', query_data[i])[0]
    			if b != 0:
        			b1 = b + 1
        			i = i + b1
    			else:
        			#print "Malformed Packet will be formed"
        			break
            	global c
        	c = i + 5

       	 	#print c
        	global qname2
        	qname2 = query_data[:c]
        	#print qname2
		global qname
		qname = query_data[:-11]
        	#print qname
		ptr = 0
		temp = []
		while True:
			count = ord(qname[ptr])
			if count == 0:
				break
			ptr += 1
			temp.append(qname[ptr:ptr+count])
			ptr += count
			global q_name1
			q_name1= '.'.join(temp)
                    	#print q_name1
        	if q_name1 == "cs5700cdn.example.com":
            		pass
        	else:
        		print "This dns only works for cs5700cdn.example.com"
               	    	sys.exit()

	def create_answer(self):

		#print "3"
		qe = Packet_form()
		#print qp
		#print id1
		#print q_name1
		header = qe.create_header(id1, 0x8180, 0x0001, 0x0001, 0X0000, 0x0001)
		#print "4"
		s1 = socket.inet_aton('54.85.32.37')
		create_ans = struct.pack('!HHHLH4s', 0xC00C , 0X0001, 0X0001, 5, 4, s1)
		total_packet = header + qname2 + create_ans
		#print total_packet
		s.sendto(total_packet, qp)
		return total_packet

a = Packet_form()
#print "1"
a.query_unpack()
a.create_answer()


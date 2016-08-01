#!/usr/bin/env python

import sys
import re


list = []
e = set()
#print 2
def general_lines_split(file1):
        file = open(file1,'rw')
        lines = file.readlines()
        for a in lines:
                b = a.split()
                list1 = list.append(b)
                #print list
        return list1
#print 1
def retrieve_unique_addresses():
        for data in list:
                d = data[8]
                #d =  c.split()
                #f = d[8]
                g = e.add(d)
                k = str(len(e))
        return "No of unique addresses contacted = "+k


def other_data(file2):
        file3 = open(file2,'rw')
        lines = file3.readlines()
        global i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0
        n = 0
        o = 0
        p = 0
        q = 0
        r = 0
        s = 0
        t = 0
        u = 0
        v = 0
        w = 0
        x = 0
        y = 0
        z = 0
        aa = 0
        bb = 0
        cc = 0
        dd = 0
        ee = 0
        ff = 0
        gg = 0
        hh = 0
        ii = 0
        jj = 0
        kk = 0
        ll = 0
        for a in lines:
                if "22smarvind" in a:
                        #global i
                        i = i+1

                if "2213E238" in a:
                        #global j
                        j = j+1


                if "Mobile/13E238" in a:
                        #global k
                        k = k+1
                if "iPhone8,1/13E238" in a:
                        #global l
                        l = l+1
                if "Arvind" in a:
                        #global m,i
                        m = m + 1
                if "3DArvind" in a:
                        cc = cc + 1
                if "batteryLevel" in a:
                        #global n
                        n = n + 1
                if "timezone" in a:
                        #global o
                        o = o + 1
                if "T-Mobile" in a:
                        #global p
                        p = p + 1
                if "0ET-Mobile" in a:
                        dd = dd + 1
                if "22T-Mobile" in a:
                        ee = ee + 1

                if "IDFA" in a:
                        #global q
                        q = q + 1
                if "deviceInfo" in a:
                        #global r
                        r = r + 1
                if "9.3.1" in a:
                        #global s
                        s = s + 1
                if "9_3_1" in a:
                        ff = ff + 1
                if "serialNumber" in a:
                        t = t + 1

                if "imei" in a:
                        u = u + 1

                if "trahkrub" in a:
                        v = v + 1

                if "projectRecon567" in a:
                        w = w + 1

                if "macaddress" in a :


                if "model=" in a:
                        y = y + 1
                if "22model" in a:
                        aa = aa + 1
                if "26model" in a:
                        bb = bb + 1
                if "Alexander" in a:
                        z = z + 1
                if "22manufacturer" in a:
                        gg = gg + 1
                if "lat=" in a:
                        hh = hh + 1
                if "lng=" in a:
                        ii = ii + 1
                if "2Czip" in a:
                        jj = jj + 1
                if "Burkhart" in a:
                        kk = kk + 1
general_lines_split(sys.argv[1])
retrieve_unique_addresses()
print retrieve_unique_addresses()
other_data(sys.argv[1])
print "emailid_leaked = ", i
print "Build_version leaked = ",j+k+l
print "Device_name leaked = ", m+cc
print "Battery_level leaked = ", n
print "timezone leaked = ", o
print "Carrier_information leaked = ", p + dd + ee
print "Advertising_ID leaked = ", q
print "Device_info leaked = ", r
print "OS_Version leaked = ",s + ff
print "Serial_Number of the phone leaked = ", t
print "IMEI_Number of the phone leaked = ", u
print "USERNAME of the ACCOUNT inplain text = ", v
print "password of the account in plain text = ", w
print "MAC_address of the phone is leaked = ", x
print "Model of the phone is leaked = ", y+aa+bb
print "Firstname of the user account leaked = ", z
print "Name of the Manufacturer leaked = ", gg
print "Latitude and Longitude info was leaked = ", hh + ii
print "Zipcode info was leaked = ", jj
print "LASTNAME was leaked = ", kk



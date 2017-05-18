#!/usr/bin/env python -u
# -*- coding: utf-8 -*-
# encoding=utf8
IPlist=['raw/src.txt','raw/dst.txt']
IPsrc=IPlist[0]
IPdst=IPlist[1]
URI_base='raw/base_uri.txt'
PORTList=[]
with open(URI_base) as UB:
    uriList = UB.readlines()
    for uri in uriList:
        port = unicode(uri.split(":").pop().rstrip('\n'),'utf-8')
        if not port.isnumeric():
            port = u"80"
        #print ('session.run("CREATE (a:port {{numport: numport}})",{{"numport": "{0}"}})').format(port)
        if not port in PORTList:
            PORTList.append(port)
for p in PORTList:
    print ('session.run("CREATE (a:port {{numport: numport}})",{{"numport": "{0}"}})').format(p)

# for i in IPlist:
#     with open(i) as f:
#         ipContents = f.readlines()
#         for ip in ipContents:
#             #session.run("CREATE (a:Person {name: {name}, title: {title}})",{"name": "Arthur", "title": "King"})
#             print('session.run("CREATE (a:box {{ip: ip}})",{{"ip": "{0}"}})').format(ip.strip('\n'))
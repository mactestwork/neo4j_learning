#!/usr/bin/env python -u
# -*- coding: utf-8 -*-
# encoding=utf8
import progressbar as pb
from neo4j.v1 import GraphDatabase, basic_auth


IPlist=['raw/src.txt','raw/dst.txt']
IPsrc=IPlist[0]
IPdst=IPlist[1]
URI_base='raw/base_uri.txt'
PORTList=[]
USER="raw/user.txt"
IPDB="localhost"
PORTBOLD="32771"
STRCONNECT="bolt://"+IPDB+":"+PORTBOLD
driver = GraphDatabase.driver(STRCONNECT, auth=basic_auth("neo4j", "neo4j"))
session = driver.session()

widgets = ['Creating port node from uri : ', pb.Percentage(), ' ', pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()]
timer = pb.ProgressBar(widgets=widgets, maxval=1000000).start()
i=0
with open(URI_base) as UB:
    uriList = UB.readlines()
    for uri in uriList:
        port = unicode(uri.split(":").pop().rstrip('\n'),'utf-8')
        if not port.isnumeric():
            port = u"80"
        i += 1
        if not port in PORTList:
            PORTList.append(port)
            timer.update(i)
for p in PORTList:
    #print ('session.run("CREATE (a:port {{numport: numport}})",{{"numport": "{0}"}})').format(p)
    session.run("CREATE (a:port {numport: $numport})",{"numport": p})
    timer.update(i)
timer.finish()


widgets = ['Creating port node from uri : ', pb.Percentage(), ' ', pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()]
timer = pb.ProgressBar(widgets=widgets, maxval=1000000).start()
i=0
for i in IPlist:
    with open(i) as f:
        ipContents = f.readlines()
        for ip in ipContents:
            #print('session.run("CREATE (a:box {{ip: ip}})",{{"ip": "{0}"}})').format(ip.strip('\n'))
            session.run("CREATE (a:box {ip: $ip})", {"ip": ip.strip('\n')})

with open (USER) as f:
    users=f.readlines()
    for u in users:
        #print('session.run("CREATE (a:user {{uName: uName}})",{{"uName": "{0}"}})').format(u.strip('\n'))
        session.run("CREATE (a:user {uName: $uName})", {"uName": u.strip('\n')})
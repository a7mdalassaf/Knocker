#!/usr/bin/env python
from scapy.all import *
from itertools import permutations
from time import sleep
import socket




def sendPkt(ip, ipsrc, port ):
        ip=IP(src=ipsrc , dst=ip)
        SYN=TCP(sport=64000 , dport=port,flags='s',seq='13345')
        send(ip/SYN)

ip = input('Des IP :')
ipsrc = input('Src IP :')
port1 = input('First port :')
port2 = input('Second port :')
port3 = input('Third port :')
ports = [port1,port2 , port3]

for port in permutations(ports):
	print(port)
	sendPkt(ip,ipsrc,port)


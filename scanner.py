# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:35:19 2021

@author: santi
Scanner
"""


import socket
import sys 
from ports import ports_and_services

def getOpenPorts(target, portRange):
    openPorts = []
    #Obtener el host con socket
    h = socket.gethostbyname(target)
    #hacer un loop sobre el rango de puertos
    for port in range(portRange[0],portRange[1]+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
    #abrir el socket determinado
        if not(sock.connect_ex((h,port))):
            openPorts.append(port)
        sock.close()
    #verificar si se conecta
    ports_and_services.fromshare(openPorts)
    #si se conecta agregarlo al array
    return openPorts





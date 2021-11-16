# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:01:12 2021

@author: santi
"""
import scanner #librería a utilizar para scannear puertos

# Ejemplo de función
ports = scanner.getOpenPorts("unam.mx",[79-82])
print("Open ports:", ports)


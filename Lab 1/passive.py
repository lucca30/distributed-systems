# -*- coding: utf-8 -*-
from socket import *


host = ''
port = 7001
wait_time_msecs = 1000


msg = ''

sckt = socket(AF_INET, SOCK_STREAM)
sckt.bind((host, port))
sckt.listen(1)

connectionSckt, address = sckt.accept()

while True:
    try: 
        msg = connectionSckt.recv(wait_time_msecs)
        connectionSckt.send(msg)
    except:
        print "The connection was closed by the active system. Turning off the passive system..."
        break

sckt.close()
connectionSckt.close()
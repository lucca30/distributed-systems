# -*- coding: utf-8 -*-
from socket import *
import time
from shared_layers import processing_layer, data_access_layer
import sys


host = ''
port = 7001
wait_time_msecs = 1000
retry_time_secs = 1


msg = ''

sckt = socket(AF_INET, SOCK_STREAM)
sckt.bind((host, port))
sckt.listen(1)

connectionSckt, address = sckt.accept()

while True:
    try: 
        msg = connectionSckt.recv(wait_time_msecs)
        print("Received:" + str(msg))
        connectionSckt.send(processing_layer(msg, data_access_layer))

    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("The connection was closed by the active system. Waiting to reconnect...")
        time.sleep(retry_time_secs)

sckt.close()
connectionSckt.close()
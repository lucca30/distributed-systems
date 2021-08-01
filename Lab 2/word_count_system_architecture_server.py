# -*- coding: utf-8 -*-
from socket import *
import time
from shared_layers import processing_layer, data_access_layer
import sys
import json

host = ''
port = 7001
wait_time_msecs = 1000
retry_time_secs = 1


msg = ''

sckt = socket(AF_INET, SOCK_STREAM)
sckt.bind((host, port))
sckt.listen(1)

connected = False
while True:
    try: 
        if(not connected):
            connectionSckt, address = sckt.accept()
            connected = True
        msg = connectionSckt.recv(wait_time_msecs)
        msg = json.loads(msg)
        print("Received:" + str(msg))
        response = processing_layer(msg['file_name'], msg['word'], data_access_layer)
        print("Response:" + str(response))
        connectionSckt.send(bytes(response,encoding='utf8'))

    except:
        print("Unexpected error:", sys.exc_info())
        print("The connection was closed by the active system. Waiting to reconnect...")
        connectionSckt.close()
        connected = False
        time.sleep(retry_time_secs)


sckt.close()

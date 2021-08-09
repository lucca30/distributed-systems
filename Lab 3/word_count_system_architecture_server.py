# -*- coding: utf-8 -*-
from socket import *
import time
from shared_layers import processing_layer, data_access_layer
import sys
import json
# import thread module
from _thread import *
  
host = ''
port = 7001
wait_time_msecs = 1000


# thread function
def threaded(c):
    while True:
        msg = c.recv(wait_time_msecs)
        if (not msg):
            break
        msg = json.loads(msg)
        print("Received:" + str(msg))
        response = processing_layer(msg['file_name'], msg['word'], data_access_layer)
        print("Response:" + str(response))
        c.send(bytes(response,encoding='utf8'))
    # connection closed
    c.close()


msg = ''

sckt = socket(AF_INET, SOCK_STREAM)
sckt.bind((host, port))
sckt.listen(1)

while True:
    try: 
        # establish connection with client
        c, addr = sckt.accept()
  
        print("Conexão adquirida, criando uma nova..")
        
        print("Nova thread!!!")
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))

    except:
        print("Unexpected error:", sys.exc_info())
        print("The connection was closed by the active system. Waiting to reconnect...")
        connected = False


sckt.close()

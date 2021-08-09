# -*- coding: utf-8 -*-
from socket import *
import time
import json

host = 'localhost'
port = 7001
retry_time_secs = 10
wait_time_msecs = 1000
msg = ''
sckt = socket()


def acquire_connection():
    connected = False 

    # Retry until is not connected
    while not connected:
        try:
            print ("Trying to acquire connection in " + str(host) + ":" +  str(port))
            sckt.connect((host, port))
            print ("   Successfully connected!")
            connected = True
        except:
            print ("Failed acquire connection in " + str(host) + ":" +  str(port))
            print ("   Trying again in " + str(retry_time_secs) + " seconds...")
            connected = False
            time.sleep(retry_time_secs)

def wait_for_message():
    msg = sckt.recv(wait_time_msecs)
    print("   Content:\n" + msg.decode("utf-8"))
        


def user_interaction():
    while True:
        file_name = input("Enter the file name, -q to quit:")
        if file_name == '-q':
            print ('The connection was closed by the user')
            break
        word = input("Enter the word to be counted:")

        sckt.send(bytes(json.dumps({'file_name':file_name, 'word':word}), encoding='utf8'))
        wait_for_message()

acquire_connection()
user_interaction()


sckt.close()
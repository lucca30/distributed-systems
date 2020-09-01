# -*- coding: utf-8 -*-
from socket import *
import time


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
            print "Trying to acquire connection in " + str(host) + ":" +  str(port)
            sckt.connect((host, port))
            print "   Successfully connected!"
            connected = True
        except:
            print "Failed acquire connection in " + str(host) + ":" +  str(port)
            print "   Trying again in " + str(retry_time_secs) + " seconds..."
            time.sleep(retry_time_secs)

def wait_for_message(start_time):
    
    msg = sckt.recv(wait_time_msecs)
    end_time = time.time()
    
    # sometimes the time to receive message is close enough to zero so the computer can't measure
    # in general, after the first message the system became faster in the exchange of messages
    total_time_waited = end_time - start_time
    print "Message received after " + "{0:.15f}".format(total_time_waited) + "s since it was sent"
    print "   Content: " + str(msg)
        


def user_interaction():
    while True:
        msg = raw_input("Write something here (-q to quit): ")
        start_time = time.time()
        sckt.send(bytes(msg))
        if msg == '-q':
            print 'The connection was closed by the user'
            break
        else:
            wait_for_message(start_time)


acquire_connection()
user_interaction()


sckt.close()
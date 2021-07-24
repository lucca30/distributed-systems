# -*- coding: utf-8 -*-
import socket
from time import sleep


host = ''
port = 7001
wait_time_msecs = 1000


msg = ''

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind((host, port))
sckt.listen(1)

print("Waiting until get a connection...")
connectionSckt, address = sckt.accept() # waits until stablishes a connection with a client
print("Connection stablished with: " + str(address[0]) + ":" + str(address[1])) 
while True:
    try: 
        msg = connectionSckt.recv(wait_time_msecs)
        print("Message received: ")
        print(msg)
        if(len(msg) == 0):
            # As you can see in this link https://man7.org/linux/man-pages/man2/recv.2.html about recv return value:
            # " ...
            #    When a stream socket peer has performed an orderly shutdown, the
            #    return value will be 0 (the traditional "end-of-file" return).
            #   ...
            #    The value 0 may also be returned if the requested number of bytes
            #    to receive from a stream socket was 0.   
            #  "
            #
            # So that's why I'm checking the len is 0 so then I will end the connection. 
            # It will only happen if the client doesnt tell us about the end of the connection
            print("The connection was probably lost and the client didn't tell us.")
            break
        print("Returning it back to the active system")
        connectionSckt.send(msg)

    # When the connection is closed by the client an exception is throwed by the library
    except socket.error:
        print("The connection was closed by the active system. Turning off the passive system...")
        break
    print("")

sckt.close()
connectionSckt.close()

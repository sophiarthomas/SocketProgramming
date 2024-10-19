# Assignment 5 - Interprocess Communication
# Sophia Thomas 029081102
# Due: 10/20/24 @ 11:55PM

import socket
import ipaddress

# Client initiates a connection

Host = input("Enter client ip address: ")

Port = int(input("Enter port: "))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpSock: 
    tcpSock.connect((Host, Port))
    
# Data is exchanged
    messaging = True

    while messaging: 
        msg = input(b"Enter a message to send the server: ")
        tcpSock.sendto(bytearray(str(msg), encoding="utf-8"), (Host, Port))
        data = tcpSock.recv(1024)
        print(f"Received {data}")
        
        session = input("Do you wish to keep this connection going then type 'yes': ")
        if session == 'yes': 
            continue
        else: 
            messaging = False


            




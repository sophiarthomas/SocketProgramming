# Assignment 5 - Interprocess Communication
# Sophia Thomas 029081102
# Due: 10/20/24 @ 11:55PM

import socket
import ipaddress

# Server sets up a listening socket

Host = '0.0.0.0'

Port = 8080

## creates listening socket (IPv4, tcp socket stream)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpSock: 
    tcpSock.bind((Host, Port)) # binds the created socket to the host and port you want to listen to 
    print(f"binding: {Host}:{Port}")
    tcpSock.listen(1) # listen to a request for the server from this socket
    print("Server is listening for connections...")

    incomingSocket, clientAddr = tcpSock.accept() 
    with incomingSocket: 
        print(f"Connected by {clientAddr}")
        while True: 
            data = incomingSocket.recv(1024) # Recieve data from client 
            if not data: 
                print("Connection Lost")
                break
            print(f"Recieved: {data.decode('utf-8')}")
            print(f"Sent: {data.upper().decode('utf-8')}")
            incomingSocket.sendall(data.upper())
	 
	
        
#import socket module
from socket import *
import time
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
# TODO start
HOST, PORT = "192.168.0.103", 1024
serverSocket.bind((HOST, PORT))
# TODO in end
while True:
    #Establish the connection
    print('Ready to serve...')
    # TODO start
    serverSocket.listen(0)
    connectionSocket, address = serverSocket.accept()
    # TODO end
    try:
        # Receive http request from the clinet
        # TODO start
        message = connectionSocket.recv(1000).decode('utf-8')
        # TODO end
        print(message)

        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        
        # Read data from the file that the client requested
        # Split the data into lines for future transmission 
        # TODO start
        outputdata = f.readlines()
        f.close()
        # TODO end
        print(outputdata)

        #Send one HTTP header line into socket
        # TODO start
        
        # send HTTP status to client
        connectionSocket.send(b'HTTP/1.1 200 OK')
        # send content type to client
        connectionSocket.send(b'Content-Type: text/html\n\n')
        
        # TODO end
        
        # Send the content of the requested file to the client  
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        # TODO start
        connectionSocket.send(b'HTTP/1.1 200 OK')
        connectionSocket.send(b'Content-Type: text/html\n\n')
        connectionSocket.send(b'404 Not Found')
        # TODO end

        #Close client socket
        # TODO start
        connectionSocket.close()
        # TODO end

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data

#import socket module
from socket import *
import time
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
# TODO start

# TODO in end
while True:
    #Establish the connection
    print('Ready to serve...')
    # TODO start
      
    # TODO end
    try:
        # Receive http request from the clinet
        # TODO start
        
        # TODO end
        print(message)

        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        
        # Read data from the file that the client requested
        # Split the data into lines for future transmission 
        # TODO start
                
        # TODO end
        print(outputdata)

        #Send one HTTP header line into socket
        # TODO start
        
        # send HTTP status to client
        
        # send content type to client
        
        # TODO end
        
        # Send the content of the requested file to the client  
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        # TODO start
        
        # TODO end

        #Close client socket
        # TODO start
        
        # TODO end
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data

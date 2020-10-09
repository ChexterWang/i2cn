import socket

# Specify the IP addr and port number 
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
HOST, PORT = 
# TODO end

while(True):
    # Listen for any request
    # TODO start
    
    # TODO end
    print("The Grading server for HW2 is running..")

    while(True):
        # Accept a new request and admit the connection
        # TODO start
        
        # TODO end
        print(str(address)+" connected")
        try:
            while (True):
                client.send(b"Welcom to the calculator server. Input your problem ?\n")
                # Recieve the data from the client and send the answer back to the client
                # Ask if the client want to terminate the process
                # Terminate the process or continue
                # TODO start
                
                # TODO end
        except ValueError:
            print("except")

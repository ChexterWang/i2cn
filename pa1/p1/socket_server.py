import socket

# Specify the IP addr and port number 
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
HOST, PORT = "127.0.0.1", 1024
# TODO end

while(True):
    # Listen for any request
    # TODO start
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(0)
    # TODO end
    print("The Grading server for HW2 is running..")

    while(True):
        # Accept a new request and admit the connection
        # TODO start
        client, address = s.accept()
        # TODO end
        print(str(address)+" connected")
        try:
            while (True):
                client.send(b"Welcom to the calculator server. Input your problem ?\n")
                # Recieve the data from the client and send the answer back to the client
                # Ask if the client want to terminate the process
                # Terminate the process or continue
                # TODO start
                ans = client.recv(1000).upper().decode('utf-8')
                client.send(b"The answer is " + ans.encode('utf-8') + b".\nDo you have any question? (Y/N)\n")
                if(client.recv(1000).upper() == b'N'):
                    client.close()
                    break
                # TODO end
        except ValueError:
            print("except")

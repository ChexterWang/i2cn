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
                prob = client.recv(1000).decode('utf-8').split()
                ans = "undefined"
                if(len(prob) == 3 and prob[0].isdigit() and prob[2].isdigit()):
                    ans = {
                        '+': lambda m,n: str(m+n),
                        '-': lambda m,n: str(m-n),
                        '*': lambda m,n: str(m*n),
                        '/': lambda m,n: str(m/n)
                    }.get(prob[1], lambda m,n: print("operator not found"))(int(prob[0]), int(prob[2]))
                else:
                    print("input is invalid")
                client.send(b"The answer is " + ans.encode('utf-8') + b".\nDo you have any question? (Y/N)\n")
                recv = client.recv(1000).upper()
                while(recv != b'Y' and recv != b'N'):
                    client.send(b"Do you have any question? (Y/N)\n")
                    recv = client.recv(1000).upper()
                if(recv == b'N'):
                    client.close()
                    break
                # TODO end
        except ValueError:
            print("except")

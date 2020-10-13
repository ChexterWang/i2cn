from socket import *
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# TODO start.
HOST, PORT = sys.argv[1], 1024
tcpSerSock.bind((HOST, PORT))
tcpSerSock.listen(0)
# TODO end.
while 1:
	# Strat receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)

	# Receive request from the client
	# TODO start.
	message = tcpCLiSock.recv(1000).decode('utf-8')
	# TODO end.
	print(message)
	
	# Extract the filename from the given message
	print(message.split()[1])
	filename = message.split()[1].partition("/")[2]
	print(filename)
	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	try:
		# Check wether the file exist in the cache
		f = open(filetouse[1:], "r")
		outputdata = f.readlines()
		fileExist = "true"
		
		# ProxyServer finds a cache hit and generates a response message
		# Send the file data to the client
		# TODO start.
		tcpCliSock.send(b'HTTP/1.1 200 OK\r\n')
        tcpCliSock.send(b'Content-Type: text/html\r\n')
        tcpCliSock.send(b'\n')
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        tcpCliSock.send(b'\r\n')
		# TODO end.

		print('Read from cache')
	# Error handling for file not found in cache
	except IOError:
		if fileExist == "false":
			# Create a socket on the proxyserver
            #TODO start
            c = socket(AF_INET, SOCK_STREAM)   
            #TODO end
            hostn = filename.replace("www.","",1)
			print(hostn)
			try:
				# Connect to the socket to webserver port 
				# TODO start.
				c.connect((hostn, 80))
				# TODO end.

				# Create a temporary file on this socket and ask webserver port for the file requested by the client
				fileobj = c.makefile('rw', None)
				fileobj.write("GET "+ filetouse + " HTTP/1.0\n\n")
				fileobj.flush()

				# Read the response into buffer
				# TODO start.
				buff = fileobj.readlines()
				# TODO end.

				# Create a new file in the cache for the requested file.
				# Also send the response in the buffer to client socket and the corresponding file in the cache
				tmpFile = open(filename,"w")
				# TODO start.
				for i in buff:
                    tmpFile.write(i)
                    tcpCliSock.send(i.encode())
                c.close()
                tmpFile.close()
				# TODO end.
			except:
				print("Illegal request")
		else:
			# HTTP response message for file not found
			# TODO start.
			tcpCliSock.send("404 Not Found")
            # TODO end.
	# Close the client sockets
	tcpCliSock.close()
# Close the server socket
# TODO start.
tcpSerSock.close()
# TODO end.

import socket

HOST, PORT = "127.0.0.1", 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
recv = s.recv(1000).decode('utf-8')
while(recv):
    s.send(input(recv).encode('utf8'))
    recv = s.recv(1000).decode('utf-8')


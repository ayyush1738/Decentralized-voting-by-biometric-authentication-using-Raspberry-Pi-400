import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("169.254.123.43", 5001))

while True:
    a=s.recv(1024).decode("utf-8")
    fp=open("details.txt","w")
    fp.write(a)
    fp.write("\n")
    fp.close()
    print(a)
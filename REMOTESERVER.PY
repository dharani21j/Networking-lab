# Networking-lab
import socket
UDP_IP_ADDRESS= "10.1.24.149"
UDP_PORT_NUMBER= 6789
ServerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerSock.bind((UDP_IP_ADDRESS,UDP_PORT_NUMBER))
print("server is listening")
while True:
 data ,addr= ServerSock.recvfrom(1024)
 print("MESSAGE:",data)

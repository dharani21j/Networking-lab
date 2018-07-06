# echo_server.py
import socket
UDP_IP_ADDRESS= "10.1.24.149"
UDP_PORT_NUMBER= 6789
message=("hello python")
bytestosend=str.encode(message)
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ClientSock.sendto(bytestosend,(UDP_IP_ADDRESS,UDP_PORT_NUMBER))

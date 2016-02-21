import socket
import cv2
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(('127.0.0.1',50058)) 

size = 1024000000
cv2.namedWindow("preview")
print "Conencted "

while True:
    data = client_socket.recv(512)
    #frame=json.loads(data)
    cv2.imshow("preview", data)

client_socket.close() 

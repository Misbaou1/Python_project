import os, socket
import cv2, base64
from sys import argv

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))
server_socket.listen(5)

client_socket, address = server_socket.accept()
print "Conencted to server - ",address,"\n"

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def get_image():
    retval, im = camera.read()
    return im
for i in xrange(ramp_frames):
    temp = get_image()  
print("Taking image...")
camera_capture = get_image()
file = "C:\Python27/test.png"
cv2.imwrite(file, camera_capture)
print("Picture taken")
del(camera)

while (1):
    data = client_socket.recv(1024)
    print "The file name received is  - ",data

    text_file = open('data.txt', "w")
    with open(data, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        text_file.write("the content is")
        text_file.write(str)

    fp = open("data.txt",'r')     # Open the data

    print "Opening"  , data
    imag = open(data, 'r')
    print "Reading the file  ", data
    while True:
        strng = imag.readline(512)
        if not strng:
            break
        client_socket.send(strng)
    #imag.close()
    print "data was succefully sent"
    exit()

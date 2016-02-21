import socket,os
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))
k = ' '
size = 1024

while(1):
    print "Enter the file name "
    fname = raw_input()
    client_socket.send(fname)
    fname = 'C:\Users\Misbaou\Desktop/'+fname
    fp = open(fname, 'w')
    while True:
        strng = client_socket.recv(512)
        if not strng:
            break
        fp.write(strng)
    fp.close()
    print "data was received"
    exit()

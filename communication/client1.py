import socket
s = socket.socket()

hostname = 'raspberrypi'
port = 9000

s.connect (('192.168.0.112',9000))

while True:
    x = input('Enter message: ')
    s.send(x.encode())
    
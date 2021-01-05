import socket

host = '192.168.0.112' # Enter IP or Hostname of your server
port = 7000 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

#Lets loop awaiting for your input
while True:
    command = input('Enter your command: ')
    if command == 'EXIT':
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))
s.close()
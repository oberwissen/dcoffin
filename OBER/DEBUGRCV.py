import socket



host = '127.0.0.1'
port = 55


s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)


s.connect(('127.0.0.1', port))


msg = s.recv(1024)


while True:
    while msg:
        print(msg.decode())
        msg = s.recv(1024)




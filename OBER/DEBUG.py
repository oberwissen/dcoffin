import socket

host = "127.0.0.1"
port = 55

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c = None

def init():
    global c
    s.bind(('', port))
    s.listen(1)
    c, addr = s.accept()
    print(f"OBERWISSEN FACTORY PANEL ---- A NEW DEBUG DEVICE CONNECTED FROM ADDR {str(addr)}")
    c.send(b"Hosgeldiniz Oberwissenfuhrer Yakup Aslantas.")

def log(log):
    global c
    c.send(log.encode())








import socket
from time import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8760))
t0 = time()
for _ in range(1000):
    sock.send('test message.'.encode('utf-8'))
    sock.recv(99)
print('time cose', time()-t0 )
sock.close()





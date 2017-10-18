
import socket
import threading
from queue import Queue
import sys
import random
import time

class nodo(threading.Thread):
    def __init__(self, ids, host, port, queue):
        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host,port))
        self.id = ids
        self.que = queue
            
    def run(self):
        while True:
            data = self.sock.recvfrom(512)
            msg = data[0].decode('ascii')
            msg = msg.split(' ')
            # print(msg)
            timestamps = int(round(time.time() * 1000))
            tempo = self.que.get()
            self.que.put(tempo)
            tempo = max(tempo, int(msg[2]))+1
            print(str(timestamps)+' '+str(tempo)+' r '+str(msg[3])+' '+msg[2])
            # rcv = data[1]
            # print(msg +'    '+ str(rcv))

def eventos():
    for i in range(0,100):
        # time.sleep(1)
        soma = cont_queue.get() + 1 
        cont_queue.put(soma)
        if (random.randrange(0,100) > 50):
            timestamps = int(round(time.time() * 1000))
            print(str(timestamps)+' '+id_host+' '+ str(soma) + ' l')
        else:
            a = nodos[random.randrange(0,len(nodos))]
            enviarEvento(nodos[mystuff][0],(a[1],a[2]))
    sys.exit(0)


def enviarEvento(idsender, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soma = cont_queue.get()
    cont_queue.put(soma)
    #              host_destino     soma            id_send
    msg = "s " + str(data[0])+' ' + str(soma) +' '+ str(idsender)
    sock.sendto(msg.encode('ascii'), data)


nodos = []
with open('nomecoisa.conf', 'r') as r:
    lines = r.readlines()
    for line in lines:
        line = line.split(' ')
        id_host = line[0]
        host = line[1]
        port = line[2]
        nodos.append((id_host, host, int(port)))

mystuff = int(sys.argv[1])

id_host = nodos[mystuff][0]
host = nodos[mystuff][1]
port = nodos[mystuff][2]

cont_queue = Queue(1)
cont_queue.put(0)
nodo = nodo(id_host, host, int(port), cont_queue) #queue deve ser a msm com todos
nodo.daemon = True
nodo.start()

eventos()
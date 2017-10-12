import socket
import threading

class nodo(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
            
    def run(self):
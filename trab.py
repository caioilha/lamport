import queue

dictop = {}
with open('nomecoisa.conf', 'r') as r:
    lines = r.readlines()
    for line in lines:
        line = line.split(' ')
        id_host = line[0]
        host = line[1]
        port = line[2]
        dictop[id_host] = {'host': host, 'port': port}

cont_queue = Queue(1)
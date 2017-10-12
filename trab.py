with open('nomecoisa.conf', 'r') as r:
    lines = r.readLines()

    for (line in lines):
        line = line.split(' ')
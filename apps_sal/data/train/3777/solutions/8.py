VALID = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def quicksum(packet):
    return 0 if set(packet) - set(VALID) else sum((VALID.index(char) * i for (i, char) in enumerate(packet, 1)))

def quicksum(packet):
    if all(True if ord(x) > 64 and ord(x) < 91 or ord(x) == 32 else False for x in packet):
        return sum(0 if x == ' ' else (ord(x) - 64) * y for y, x in enumerate(packet,1))
    return 0

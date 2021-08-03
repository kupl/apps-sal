def quicksum(packet):
    alph = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    su = 0

    for k, v in enumerate(packet):
        if v not in alph:
            return 0
        su += (k + 1) * alph.index(v)
    return su

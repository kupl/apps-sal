def encode(s):
    if len(s)<=1: return s,0
    mas = sorted([s[-i:]+s[:-i] for i in range(0,len(s))])
    return ''.join([c[-1] for c in mas]), mas.index(s)

def decode(sn, n):
    if len(sn)<=1: return sn
    table = [""] * len(sn)
    for j in range(len(sn)): table = sorted(sn[i] + table[i] for i in range(len(sn))) 
    return table[n]


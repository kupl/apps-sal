import re

def moveBishop(bs, deltas):
    posBishops = []
    for b,coef in zip(bs, [-1,1]):
        while True:
            tmpPos = ''.join( chr(ord(l) + coef*direc) for l,direc in zip(b, deltas) )
            if not bool(re.match(r'[a-h][1-8]', tmpPos)): break
            b = tmpPos
        posBishops.append(b)
    return posBishops
    
def bishop_diagonal(*args):
    bishops = sorted(args)
    deltas = [ ord(b) - ord(a) for a,b in zip(*bishops) ]
    return moveBishop(bishops, list(map(lambda v: v//abs(v), deltas))) if len(set(map(abs, deltas))) == 1 else bishops

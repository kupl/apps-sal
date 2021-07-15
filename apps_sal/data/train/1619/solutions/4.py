import math

def decompose_aux(nb, rac):
    if (nb == 0):
        return [] 
    i = rac
    l = None
    while (i >= int(math.sqrt(nb / 2.0)) + 1):
        diff = nb - i * i
        rac = int(math.sqrt(diff))
        l = decompose_aux(diff, rac);
        if l != None: 
            l.append(i)
            return l
        i -= 1
    return l
    
def decompose(n):
    l = decompose_aux(n * n, int(math.sqrt(n * n - 1)))
    if l != None:
        return l 
    else:
        return None

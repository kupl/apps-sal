import math

def branch(n):
    l = (math.sqrt(n)+1)//2
    d = n-(2*l-1)**2
    if d == 0:
        if l == 1:
            return 0
        else:
            return 3
    else:
        return int((d-1)/(2*l))

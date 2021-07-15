from itertools import count

def pos(n):
    for i in count(1, 2):
        if i*i >= n:
            break
    n -= (i - 2) ** 2
    step = i - 1
    p = (1+1j) * (step//2)
    for d in [-1, -1j, +1, +1j]:
        x = min(step, n)
        p += x * d
        n -= x
    return p
    
    
def distance(n):
    p = pos(n)
    return abs(int(p.real)) + abs(int(p.imag))

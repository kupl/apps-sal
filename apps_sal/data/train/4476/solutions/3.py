import math
def check(nr):    
    lim = int(nr ** 0.5)
    x = 0
    if nr == 2 or nr == 3:
        return True
    if nr % 2 == 0 or nr <= 1:
        return False
    if nr < 9:
        return True
    if nr % 3 == 0:
        return False
    i = 5
    while i <= lim:
        if nr % i == 0:
            return False
        if nr % (i + 2) == 0:
            return False
        i += 6
    return True
    
def biggest(nr):
    return (len(str(nr)) - 1) or 1

def count_even(nr):
    r = 0
    for i in str(nr):
        r += (int(i) % 2 == 0)
    return r
    
def f(n):
    nr = n - 1
    res = 0
    cmax = (0,0)
    while nr > 0:
        if check(nr):
            e = count_even(nr)
            b = biggest(nr)
            if e > cmax[0]:
                cmax = (e,nr)
            if b == cmax[0]:
                return cmax[1]
        nr -= 1



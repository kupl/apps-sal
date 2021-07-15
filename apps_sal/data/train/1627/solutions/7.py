CHARS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def to_dec(s,b):
    n = 0
    for i,v in enumerate(s[::-1]):
        n += CHARS.index(v)*b**i
    return n

def to_base(n,b):
    r = ''
    while n >= b:
        n,x = divmod(n,b)
        r += CHARS[:b][x]
    r += CHARS[:b][n]
    return r[::-1]
         
def is_polydivisible(s,b):
    return all(not to_dec(s[:i],b)%i for i in range(1,len(s)+1))

def get_polydivisible(x,b):
    c = 0
    n = 0
    while c<x:
        try:
            if is_polydivisible(to_base(n,b),b):
                c += 1
        except:
            pass
        n += 1
    return to_base(n-1,b) or '0'

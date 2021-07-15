CHARS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def from10(n, b):
    if b == 10: return n
    new = ''
    while n: 
        new += str(CHARS[n%b])
        n //= b
    return new[::-1]

def to10(n, b):
    num = 0
    for i, d in enumerate(str(n)[::-1]):
        num += int(CHARS.index(d))*(b**i)
    return num

def is_polydivisible(s, b):
    for i in range(1, len(s)+1):
        if to10(s[:i], b) % i != 0: return False
    return True


def get_polydivisible(n, b):
    if n == 1: return '0'
    i = 0 
    poly = []
    while len(poly) < n:
        fr = str(from10(i, b))
        if is_polydivisible(str(fr), b): 
            poly.append(fr)
            i += 1
        else: i += 1
    return poly[-1]

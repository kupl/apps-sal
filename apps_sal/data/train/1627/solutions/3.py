b62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def atoi (n, b):
    res = 0
    n = str(n)
    for i,c in enumerate(n):
        res += b62.index(c) * b**(len(n)-i-1)
    return res
    
def itoa (n, b):
    res = ""
    while n > 0:
        res = b62[n % b] + res
        n //= b
    return res or "0"

def is_polydivisible(s, b):
    for i in range(len(s), 0, -1):
        n = atoi(s[:i], b)
        if n % i != 0:
            return False
    return True

def get_polydivisible(n, b):
    res = ""
    c = 0
    for i in range(n):
        while 1:
            a = itoa(c, b)
            c += 1
            if is_polydivisible(a, b):
                res = a
                break
    return res

def j(n,k):
    i = 1
    for f in range(1,k) : i *= f + n
    for f in range(1,k) : i //= f
    return i
def multiply(n,k):
    i = f = 1
    while f * f < n :
        l,f = 0,-~f
        while n % f < 1 : l,n = -~l,n // f
        if l : i *= j(l,k)
    return i * (n < 2 or j(1,k))

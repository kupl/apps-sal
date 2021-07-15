def digitize(n):
    n = str(n)
    n = list(n)
    n = list(map(conv, n))
    n.reverse()
    return n
    

def conv(x):
    return int(x)

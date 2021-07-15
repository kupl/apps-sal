def choose(n, k):
    return prod(n-k, n)//prod(1, k)

def prod(f, t):
    if f == t:
        return 1
    return t * prod(f, t-1)

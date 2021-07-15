def prime(x):
    if x < 3 or not x%2: return x==2
    return all(x%i for i in range(3, int(x**0.5)+1, 2))

D = {}
def gap(g, m, n):
    get = lambda x: D[x] if x in D else D.setdefault(x, prime(x))
    for i in range(m, n-g+1):
        if get(i) and get(i+g) and not any(map(get, range(i+1, i+g))):
            return [i, i+g]

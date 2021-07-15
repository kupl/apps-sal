def primes(n):
    primes = [2]
    for i in range(3,n+1):
        if all(i%p!= 0 for p in primes) == True:
            primes.append(i)
    return(primes)
def decomp(n):
    prim = primes(n)
    factors = {}
    for i in range(2, n+1):
        if i in prim:
            factors[i] = 1
        else:
            for p in prim:
                while i%p == 0:
                    factors[p] += 1
                    i /= p
                if i == 1:
                    break
    res = ''
    for x, y in factors.items():
        res += '{0}^{1} * '.format(x,y) if y != 1 else '{0} * '.format(x)
    return(res[:-3])

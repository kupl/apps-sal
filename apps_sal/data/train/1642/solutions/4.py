from scipy.special import comb

def multiply(n, k):
    r, d = 1, 2
    while d * d <= n:
        i = 0
        while n % d == 0:
            i += 1
            n //= d
        if i: r *= comb(i + k - 1, k - 1, exact=True)
        d += 1
    if n > 1: 
        r *= k
    return r

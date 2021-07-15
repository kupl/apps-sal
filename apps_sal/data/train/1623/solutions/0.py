from fractions import Fraction as frac
def ber():
    res, m = [], 0
    while True:
        res.append(frac(1, m+1))
        for j in range(m, 0, -1):
          res[j-1] = j*(res[j-1] - res[j])
        yield res[0]
        m += 1
def bernoulli_number(n):   
    if n == 1: return Fraction(-1, 2)
    if n % 2 == 1: return 0
    bn2 = [ix for ix in zip(range(n + 2), ber())]
    bn2 = [b for _, b in bn2]
    return bn2[n]

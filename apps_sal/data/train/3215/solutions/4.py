def _coefs(l):
    n = 1
    for i in range(l):
       yield n
       n = n * (l-i-1) // (i+1)
    yield n

def reduce_pyramid(base):
    coefs = _coefs(len(base))
    return sum(next(coefs)*n for n in base)

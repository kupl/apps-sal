import math

def PrimeFactorsSum(nr):
    res = []
    s = 1
    for i in range(2,int(math.sqrt(nr) + 1)):
        cs = 1
        ct = 1
        while nr % i == 0:
            res.append(i)
            nr //= i
            ct *= i
            cs += ct
        s *= cs
    if nr > 2:
        s *= (nr + 1)
        res.append(nr)
    if res and s % sum(res) == 0:
        return True
    return False

def ds_multof_pfs(nMin, nMax):
    res = []
    i = nMin
    while i <= nMax:
        if PrimeFactorsSum(i):
            res.append(i)
        i += 1
    return res

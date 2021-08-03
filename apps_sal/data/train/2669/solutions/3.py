def sumIntegers(n):
    mod = 10
    lst = []
    while n > 0:
        lst.append(n % mod)
        n -= n % mod
        n //= 10
    result = 1
    for i in lst:
        if i != 0:
            result *= i
    return result


def convergence(n):
    ntest = 1
    i = 0
    while True:
        if ntest == n:
            return i
        elif n > ntest:
            ntest = ntest + sumIntegers(ntest)
        else:
            n = n + sumIntegers(n)
            i += 1

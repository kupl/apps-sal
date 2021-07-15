import math
def factors(n):
    f = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                f.append(i)
                n = n // i
                break
    return f

def factor_sum(n):
    f = factors(n)
    last = sum(f)
    while n != f[0]:
        n = sum(f)
        f = factors(n)
        if f == last:
           return n
        last = f
    return n

from math import factorial
def perms(e):
    e = str(e)
    n = factorial(len(e))
    for i in (e.count(i) for i in set(e) if e.count(i)>1):
        if i:
            n = n / factorial(i)
    return n

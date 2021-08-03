import math


def eq_root(s):
    return int((-1 + math.sqrt(1 + 4 * s)) / 2)


def nc2(n):
    return int(n * (n - 1) / 2)


def chefina(n):
    s = int(n * (n + 1) / 2)
    if s % 2 != 0:
        return 0
    count = 0
    x = eq_root(s)
    count += n - x
    if 2 * x * (x + 1) == n * (n + 1):
        count += nc2(x) + nc2(n - x)
    return count


try:
    tstc = int(input())
    for t in range(tstc):
        n = int(input())
        print(chefina(n))
except:
    pass

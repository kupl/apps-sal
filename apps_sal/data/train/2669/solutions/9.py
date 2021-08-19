from functools import reduce


def convergence(n):
    j = 0
    x = 1
    s1 = set()
    s2 = set()
    while True:
        s1.add(x)
        s2.add(n)
        if x in s2 or n in s1 or s1.intersection(s2):
            break
        if n < 10:
            n = n + n
        else:
            n = n + reduce(lambda h, k: h * k, (int(i) for i in str(n) if i != '0'))
        if x < 10:
            x = x + x
        else:
            x = x + reduce(lambda h, k: h * k, (int(i) for i in str(x) if i != '0'))
    return sorted(list(s2)).index(list(s1.intersection(s2))[0])

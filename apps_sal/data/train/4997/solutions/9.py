def f(n):
    r = 1 + n
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            r += i
            j = n // i
            if i != j:
                r += j
    return r


s = set()
for i in range(528, 10000):
    j = int(str(i)[::-1])
    if i != j and f(i) == f(j):
        s |= {i, j}


def equal_sigma1(n):
    return sum((x for x in s if x <= n))

def sigma(n):
    r = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            r += i + n // i
    if n ** 0.5 % 1 != 0:
        return r
    else:
        return r - int(n ** 0.5)


def equal_sigma1(nmax):
    (i, s) = (2, 0)
    while i <= nmax:
        rev = int(str(i)[::-1])
        if i != rev and sigma(i) == sigma(rev):
            s += i
        i += 1
    return s

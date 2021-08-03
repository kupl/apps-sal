def f(n):
    r = 1
    c = 0
    pf = primef(n)
    pf.append(-1)
    m = pf[0]
    for i in pf:
        if i == m:
            c += 1
        else:
            r *= c * m**(c - 1)
            m = i
            c = 1
    return r


def primef(n):
    i = 2
    f = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            f.append(i)
    if n > 1:
        f.append(n)
    return f

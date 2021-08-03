def sflpf_data(val, nMax):
    r = []
    for i in range(2, nMax):
        fac = primef(i)
        if len(fac) > 1 and fac[0] + fac.pop() == val:
            r.append(i)
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

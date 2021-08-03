def mobius(n):
    sP, p = set(), 2
    while n > 1 and p <= n**.5:
        while not n % p:
            if p in sP:
                return 0
            sP.add(p)
            n //= p
        p += 1 + (p != 2)
    return (-1)**((len(sP) + (n != 1)) % 2)

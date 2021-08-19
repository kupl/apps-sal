def mult_primefactor_sum(a, b):
    ret = []
    for m in range(a, b + 1):
        (p, s, n) = (2, 0, m)
        while n > 1 and p <= n ** 0.5:
            while n % p == 0:
                s += p
                n //= p
            p += 1
        s += n > 1 and n
        if s < m and m % s == 0:
            ret.append(m)
    return ret

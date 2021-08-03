def prod_int_partII(n, s, min_=2):
    total, fac = 0, []
    for d in range(min_, int(n ** .5) + 1):
        if not n % d:
            count, l, sub = prod_int_partII(n // d, s - 1, d)
            if l == 1:
                sub = [sub]
            total += count + 1
            fac.extend([d] + x for x in sub)
    if s == 1:
        fac = [[n]]
    return [total, len(fac), fac[0] if len(fac) == 1 else fac]

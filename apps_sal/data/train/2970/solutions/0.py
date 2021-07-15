def prod_int_part(n, min_=2):
    total, fac = 0, []
    for d in range(min_, int(n ** .5) + 1):
        if not n % d:
            count, sub = prod_int_part(n // d, d)
            total += count + 1
            if not count: sub = [n // d]
            if not fac: fac = [d] + sub
    return [total, fac]

def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    elif n >= m:
        return 0
    else:
        mult = 1
        i = 1
        n_mult = 0
        while mult <= m: 
            mult = i * n
            if mult >= m:
                return n_mult
            n_mult += mult
            i += 1 
        return n_mult


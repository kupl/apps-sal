def zeroes(base, number):
    pzeros = []
    for p in range(2, base + 1):
        e = 0
        while base % p == 0:
            base /= p
            e += 1
        if e:
            (f, m) = (0, number)
            while m:
                m /= p
                f += m
            pzeros.append(f / e)
    return min(pzeros)

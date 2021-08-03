def array_equalization(a, n):
    MIn, l = [], len(a)
    for X in a:
        i, pa, c = 0, a[:], 0
        while i < len(pa):
            if pa[i] != X:
                pa[i:i + n] = [X] * min(n, l)
                c += 1
            i += 1
        MIn.append(c)
    return min(MIn)

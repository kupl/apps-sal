def combs(comb1, comb2):
    n1, n2 = len(comb1), len(comb2)
    c1 = int(comb1.replace('*', '1').replace('.', '0'), 2)
    c2 = int(comb2.replace('*', '1').replace('.', '0'), 2)
    return min(next(max(n1, i + n2) for i in range(1, 11) if c1 & (c2 << i) == 0),
               next(max(n2, i + n1) for i in range(1, 11) if c2 & (c1 << i) == 0))

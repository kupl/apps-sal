def hamming_distance(a, b):
    p = len(bin(max(a, b)))
    return sum(i != j for i, j in zip(bin(a)[2: ].rjust(p, '0'), bin(b)[2:].rjust(p, '0')))

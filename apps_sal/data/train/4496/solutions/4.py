def hamming_distance(a, b):
    return sum(y != x for y, x in zip(b, a))

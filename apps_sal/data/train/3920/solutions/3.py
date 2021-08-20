def hamming_distance(a, b):
    return sum((x != y for (x, y) in zip(format(a, '020b'), format(b, '020b'))))

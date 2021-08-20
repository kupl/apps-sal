def hamming_distance(a, b):
    return sum((b1 != b2 for (b1, b2) in zip(a, b)))

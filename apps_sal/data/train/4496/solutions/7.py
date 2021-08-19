def hamming_distance(a, b):
    return sum((ca != cb for (ca, cb) in zip(a, b)))

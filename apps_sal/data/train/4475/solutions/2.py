def find(seq):
    a, b, c = max(seq), min(seq), len(seq)
    z = list(range(b, a, (a - b) // c))
    return list(set(z) - set(seq))[0]

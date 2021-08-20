def next_higher(x):
    return x + (x & -x) | (x ^ x + (x & -x)) // (x & -x) >> 2

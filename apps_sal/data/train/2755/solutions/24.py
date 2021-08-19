def multiple_of_index(a):
    return [n for (i, n) in enumerate(a) if i >= 1 > n % i]

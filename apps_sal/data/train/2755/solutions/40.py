def multiple_of_index(a):
    return [n for (i, n) in enumerate(a) if i and (not n % i)]

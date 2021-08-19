def multiple_of_index(a):
    return [v for (i, v) in enumerate(a) if i and v % i == 0]

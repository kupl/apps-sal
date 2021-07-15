def find_multiples(d, l):
    return list(filter(lambda x: x % d == 0, range(1, l + 1)))

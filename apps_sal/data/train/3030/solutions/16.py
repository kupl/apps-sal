def nb_dig(n, d):
    return sum([1 if str(d) in a else 0 for x in range(n + 1) for a in str(x * x)])

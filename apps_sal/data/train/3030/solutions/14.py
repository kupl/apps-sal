def nb_dig(n, d):
    return sum([str(k * k).count(str(d)) for k in range(n + 1)])

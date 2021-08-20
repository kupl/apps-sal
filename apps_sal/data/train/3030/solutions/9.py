def nb_dig(n, d):
    return sum((str(i ** 2).count(str(d)) for i in range(n + 1)))

def nb_dig(n, d):
    return sum(str(i * i).count(str(d)) for i in range(n + 1))

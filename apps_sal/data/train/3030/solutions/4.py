def nb_dig(n, d):
    return ''.join(str(n * n) for n in range(n + 1)).count(str(d))

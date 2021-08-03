def nb_dig(n, d):
    return str([n**2 for n in range(n + 1)]).count(str(d))

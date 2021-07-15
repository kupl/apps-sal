def nb_dig(n, d):
    return sum(str(num**2).count(str(d)) for num in range(n + 1))

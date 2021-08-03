def nb_dig(n, d):
    s = str(d)
    return sum(sum(c == s for c in str(k**2)) for k in range(n + 1))

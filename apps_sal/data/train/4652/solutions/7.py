def score(n):
    return n and 2 ** (len(bin(n)) - 2) - 1

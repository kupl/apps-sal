def sxore(n):
    res = {0: n, 1: 1, 2: n + 1, 3: 0}
    return res[n % 4]

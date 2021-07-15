def nthterm(first, n, c):
    if n == 0:
        return first
    else:
        return nthterm(first + c, n - 1, c)

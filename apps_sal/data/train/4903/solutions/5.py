def nthterm(first, n, d):
    return first if n == 0 else nthterm(first + d, n - 1, d)

def count_sheep(n):
    return n and count_sheep(n - 1) + str(n) + ' sheep...' or ''

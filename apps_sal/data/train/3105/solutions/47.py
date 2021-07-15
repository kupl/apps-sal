count_sheep = lambda n: n and count_sheep(n - 1) + str(n) + ' sheep...' or ''

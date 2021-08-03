def rocks(n):
    ini, c = '9' * (len(str(n)[:-1])), 0
    while ini:
        c += (n - int(ini)) * len(str(n))
        n, ini = int(ini), ini[:-1]
    return c + n

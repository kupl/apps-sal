def count_sheep(n):
    sheep = ''
    for m in range(1,n + 1):
        sheep = sheep + str(m) + ' sheep...'
    return sheep

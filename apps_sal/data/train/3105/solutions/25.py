def count_sheep(n):
    sheep = ''
    for x in range(1, n + 1):
        sheep += f'{x} sheep...'
    return sheep

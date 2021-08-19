def count_sheep(n):
    l = []
    for x in range(1, n + 1):
        l.append(f'{x} sheep...')
    return ''.join(l)

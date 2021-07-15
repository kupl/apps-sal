def count_sheep(n):
    list_sheep = []
    for i in range(1, n + 1):
        list_sheep.append(f'{i} sheep...')
    return ''.join(list_sheep)


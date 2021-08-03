def count_sheep(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(f'{i} sheep...')
    return ''.join(arr)

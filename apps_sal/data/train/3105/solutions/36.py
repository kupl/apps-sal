def count_sheep(n):
    result = []
    for i in range(n):
        result.append(f'{i + 1} sheep...')
    return ''.join(result)

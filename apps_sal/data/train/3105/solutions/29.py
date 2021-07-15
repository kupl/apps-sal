def count_sheep(n):
    empty = []
    for num in range(1,n+1):
        empty.append(f'{num} sheep...')
    return ''.join(empty)

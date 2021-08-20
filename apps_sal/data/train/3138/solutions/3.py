def climb(n):
    return [n >> i for i in range(len(f'{n:b}') - 1, -1, -1)]

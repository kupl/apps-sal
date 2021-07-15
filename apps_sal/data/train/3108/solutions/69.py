def multi_table(n):
    return '\n'.join(f'{m} * {n} = {m*n}' for m in range(1, 11))

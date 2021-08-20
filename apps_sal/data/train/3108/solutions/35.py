def multi_table(n):
    r = f'1 * {n} = {n}'
    for i in range(2, 11):
        r += f'\n{i} * {n} = {i * n}'
    return r

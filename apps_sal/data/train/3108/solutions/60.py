def multi_table(n):
    return ''.join(f'{i} * {n} = {i*n}\n' for i in range(1, 11)).rstrip('\n')

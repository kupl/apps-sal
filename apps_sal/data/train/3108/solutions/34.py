def multi_table(n):
    table = []
    for i in range(1, 11):
        table.append(f'{i} * {n} = {i * n}')
    string = '\n'.join(table)
    return string

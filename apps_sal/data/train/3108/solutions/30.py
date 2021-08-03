def multi_table(number):
    lst = []

    for i in range(1, 11):
        item = f'{i} * {number} = {i * number}'
        lst.append(item)

    return '\n'.join(lst)

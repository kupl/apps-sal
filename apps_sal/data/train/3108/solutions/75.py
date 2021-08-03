def multi_table(number):
    st = ''
    for i in range(1, 11):
        res = i * number
        if i == 1:
            st = st + f'{i} * {number} = {res}'

        else:
            st = st + f'\n{i} * {number} = {res}'
    return st

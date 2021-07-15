def multi_table(number):
    m = []
    for i in range(1,11):
        m.append(f'{i} * {number} = {i * number}')
        w = "\n".join(m)
    return w


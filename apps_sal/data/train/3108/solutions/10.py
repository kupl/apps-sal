def multi_table(number):
    return '\n'.join(f'{n} * {number} = {number*n}' for n in range(1, 11))

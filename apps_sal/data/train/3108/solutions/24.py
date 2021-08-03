def multi_table(number):
    return '\n'.join(f"{i} * {number} = {number*i}" for i in range(1, 11))

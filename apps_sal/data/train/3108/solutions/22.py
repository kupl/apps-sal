def multi_table(number):
    return '\n'.join(f'{num} * {number} = {num * number}' for num in range(1, 11))

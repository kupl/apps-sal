def multi_table(number):
    arr = [f'{i + 1} * {number} = {(i + 1) * number}' for i in range(10)]
    return '\n'.join(arr)

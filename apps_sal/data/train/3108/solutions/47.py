def multi_table(number):
    arr = []
    for i in range(1, 11):
        arr.append('{} * {} = {}'.format(i, number, i * number))
    return '\n'.join(arr)

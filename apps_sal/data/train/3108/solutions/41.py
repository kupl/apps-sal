def multi_table(number):
    index = 1
    k = ''
    while True:
        if index <= 10:
            k += '{} * {} = {}\n'.format(index, number, index * number)
        else:
            break
        index += 1
    return k[:-1]

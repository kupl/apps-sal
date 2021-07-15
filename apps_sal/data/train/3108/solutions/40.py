def multi_table(number):
    r = []
    for i in range(1,11):
        r.append('{} * {} = {}'.format(i, number, i*number))
    return '\n'.join(r)

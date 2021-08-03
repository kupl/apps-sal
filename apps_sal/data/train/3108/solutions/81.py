def multi_table(num):
    return '\n'.join(['%d * %d = %d' % (i, num, i * num) for i in range(1, 11)])

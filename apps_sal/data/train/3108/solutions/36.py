def multi_table(number):
    return '\n'.join(('%d * %d = %d' % (i, number, i * number) for i in range(1, 11))).rstrip()

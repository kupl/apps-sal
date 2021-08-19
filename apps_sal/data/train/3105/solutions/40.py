def count_sheep(n):
    a = ''
    return ''.join((a + str(i + 1) + ' sheep...' for i in range(n)))

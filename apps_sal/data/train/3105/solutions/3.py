def count_sheep(n):
    return ''.join(('%d sheep...' % (i + 1) for i in range(n)))

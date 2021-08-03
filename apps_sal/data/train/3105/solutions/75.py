def count_sheep(n):
    x = ''
    for i in range(1, n + 1):
        x += '%d sheep...' % i
    return x

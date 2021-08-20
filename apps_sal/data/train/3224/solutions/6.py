def binary_pyramid(m, n):
    sm = 0
    for i in range(m, n + 1):
        sm += int('{0:b}'.format(i))
    return '{0:b}'.format(sm)

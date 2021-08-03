def binary_pyramid(m, n):
    return '{:b}'.format(sum(map(int, map('{:b}'.format, range(m, n + 1)))))

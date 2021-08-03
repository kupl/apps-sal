def binary_pyramid(m, n):
    return format(sum(int(format(i, 'b')) for i in range(m, n + 1)), 'b')

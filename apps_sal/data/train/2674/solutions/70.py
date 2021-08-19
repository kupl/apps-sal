def two_sort(array):
    return ''.join((sorted(array)[0][i] + '***' for i in range(0, len(sorted(array)[0]))))[:-3]

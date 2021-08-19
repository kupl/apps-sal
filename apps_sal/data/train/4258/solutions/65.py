import decimal


def series_sum(n):
    return '%.2f' % sum((1 / (1 + 3 * i) for i in range(n)))

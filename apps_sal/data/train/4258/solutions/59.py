def series_sum(n):
    result = 1 + 1 / 4
    a = 4
    if n == 1:
        return str('%.2f' % n)
    elif n == 0:
        return str('%.2f' % 0)
    for i in range(1, n - 1):
        result += 1 / (a + i * 3)
    return str('%.2f' % result)

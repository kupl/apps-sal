def series_sum(n):
    sum = 0
    if n == 1:
        return '1.00'
    else:
        for i in range(n):
            sum += 1 / (1 + 3 * i)
    return str('%.2f' % sum)

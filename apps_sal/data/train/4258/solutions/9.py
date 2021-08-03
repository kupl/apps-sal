def series_sum(n):
    result = 0
    for i in range(0, n):
        result += (1 / (1 + 3 * i))
    return "{number:.{digits}f}".format(number=result, digits=2)

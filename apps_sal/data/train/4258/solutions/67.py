def series_sum(n):
    if n == 0:
        return '0.00'
    else:
        numerator = 1
        denom = 1
        output = ''
        num = 0.0
        for i in range(n):
            num += numerator / denom
            denom += 3
            output = str(format(round(num, 2), '.2f'))
        return output

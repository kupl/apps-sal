def series_sum(n):
    if n == 0:
        return '0.00'
    return '%0.2f' % float(str(1 + sum(1/(1+i*3) for i in range(1,n))))

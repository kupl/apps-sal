def series_sum(n):
    sum = 0
    for i in range(0, n):
        sum += 1/(1+i*3)
    return str(format(sum, '.2f'))

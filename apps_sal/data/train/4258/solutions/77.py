def series_sum(n):
    sum = 1
    if n > 1:
        for i in range(n - 1):
            sum += (1 / (4 + (3 * i)))
    return str("{:.2f}".format(round(sum,2))) if n > 0 else "0.00"


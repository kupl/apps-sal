def series_sum(n):
    if n == 0:
        return "0.00"
    if n == 1:
        return "1.00"
    sum = 1.00
    for i in range(n - 1):
        sum = sum + 1 / (4 + (3 * i))
    return "{:.2f}".format(sum)

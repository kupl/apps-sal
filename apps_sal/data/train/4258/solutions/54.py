def series_sum(n=0):
    sum = 0.00
    num = 1
    for i in range(n):
        sum += 1 / num
        num += 3
    return ((str(round(sum, 2))) + "0")[:4]

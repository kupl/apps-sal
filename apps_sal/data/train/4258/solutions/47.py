def series_sum(n):
    sum = 0
    div = 1

    for i in range(n):
        sum += 1 / div
        div += 3
    if n == 0:
        return str(n) + '.00'
    elif len(str(round(sum, 2))) < 4:
        return str(round(sum, 2)) + "0"
    else:
        return str(round(sum, 2))

def series_sum(n):
    if n == 0:
        return "0.00"
    if n == 1:
        return "1.00"
    elif n == 2:
        return "1.25"
    else:
        sum = 1.25
        i = 4
        for loop in range(n - 2):
            i = i + 3
            sum = sum + 1 / i
    return "{:.2f}".format(sum)

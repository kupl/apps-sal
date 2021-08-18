def series_sum(n):
    sum = float()
    j = 1
    for i in range(n):
        sum += (1 / j)
        j += 3
    result = str(round(sum, 2))
    if len(result) == 3:
        return result + '0'
    else:
        return result

def doubles(maxk, maxn):
    result = 0
    for k in range(1, maxk + 1):
        curr_sum = 0
        for n in range(1, maxn + 1):
            curr_sum += 1 / (n + 1) ** (2 * k)
        result += 1 / k * curr_sum
    return result

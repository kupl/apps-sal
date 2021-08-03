def sum_triangular_numbers(n):
    if n < 0:
        return 0
    res = [1]
    i = 2
    for x in range(n - 1):
        res.append(res[-1] + i)
        i += 1
    return sum(res)

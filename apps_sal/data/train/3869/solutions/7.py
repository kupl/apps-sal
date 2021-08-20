def shape_area(n):
    res = 1
    for x in range(1, n):
        res += x * 4
    return res

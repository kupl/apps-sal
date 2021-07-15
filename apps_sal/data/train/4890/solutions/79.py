def find_difference(a, b):
    res1 = a[0] * a[1] * a[2]
    res2 = b[0] * b[1] * b[2]
    if res2 > res1:
        res = res2 - res1
    else:
        res = res1 - res2
    return res

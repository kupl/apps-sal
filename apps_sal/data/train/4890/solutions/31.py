def find_difference(a, b):
    res1 = 1
    res2 = 1
    for n in a:
        res1 *= n
    for n in b:
        res2 *= n
    return abs(res1 - res2)

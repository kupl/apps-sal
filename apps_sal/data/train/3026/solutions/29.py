def min_value(digits):
    res = 0
    for item in sorted(set(digits)):
        res = res * 10 + item
    return res

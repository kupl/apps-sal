def min_value(digits):
    digits = list(set(digits))
    res = ''
    while len(digits) > 0:
        min_num = min(digits)
        res += str(min_num)
        digits.remove(min_num)
    return int(res)

def min_value(digits):
    digits = list(dict.fromkeys(digits))
    print(digits)
    res = ''
    for i in list(sorted(digits)):
        res += str(i)
    return int(res)

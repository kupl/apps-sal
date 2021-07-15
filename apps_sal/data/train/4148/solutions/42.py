def sum_digits(number):
    num = str(abs(number))
    res = 0
    for item in num:
        res += int(item)
    return res

def min_value(digits):
    number = list(dict.fromkeys(digits))
    number.sort()
    return int(''.join(str(i) for i in number))

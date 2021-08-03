def min_value(digits):
    digits.sort()
    digits = list(dict.fromkeys(digits))

    if digits[0] == 0:
        aux = digits[0]
        digits[0] = digits[1]
        digits[1] = aux

    number = 0
    for i in digits:
        number = number * 10 + i

    return number

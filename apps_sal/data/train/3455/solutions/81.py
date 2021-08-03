def disarium_number(number):
    digits = []
    numberc = number
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10
    digit = []
    while len(digits) > 0:
        digit.append(digits.pop())
    tot = 0
    i = 0
    while i < len(digit):
        term = digit[i]**(i + 1)
        tot = tot + term
        i = i + 1
    if tot == numberc:
        return "Disarium !!"
    else:
        return "Not !!"

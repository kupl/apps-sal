def fact(n):
    p = 1
    while n > 0:
        p = p * n
        n = n - 1
    return p


def strong_num(number):
    tot = 0
    numberc = number
    while number > 0:
        digit = number % 10
        tot = tot + fact(digit)
        number = number // 10
    if tot == numberc:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'

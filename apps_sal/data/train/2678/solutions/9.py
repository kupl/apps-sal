def is_digit(p):
    return p >= '0' and p <= '9'


def is_sign(p):
    return p in '+-*/^%'


def calc(sign, a, b):
    try:
        if sign == '+':
            return a + b
        elif sign == '-':
            return a - b
        elif sign == '*':
            return a * b
        elif sign == '/':
            return a // b
        elif sign == '^':
            return a ** b
        else:
            return a % b
    except:
        return None


def no_order(equation):
    (left, right) = (0, '')
    sign = '+'
    for e in equation:
        if is_sign(e):
            left = calc(sign, left, int(right))
            right = ''
            if left == None:
                return None
            sign = e
        elif is_digit(e):
            right += e
        elif e != ' ':
            return None
    return calc(sign, left, int(right))

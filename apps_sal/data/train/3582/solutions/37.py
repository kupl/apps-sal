def is_digit(n):
    digits = '0123456789'
    return n in digits if len(n) == 1 else False

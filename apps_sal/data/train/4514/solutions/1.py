def int_to_negabinary(i):
    i, s = -i, ''
    while i:
        i, r = divmod(i, -2)
        s += str(-r)
    return s[::-1] or '0'


def negabinary_to_int(s):
    i, b = 0, 1
    for c in s[::-1]:
        i += int(c) * b
        b *= -2
    return i

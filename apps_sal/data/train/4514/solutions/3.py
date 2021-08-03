def int_to_negabinary(n):
    return int_to_negabinary(n // -2 + n % 2).lstrip('0') + str(n % 2) if n else '0'


def negabinary_to_int(s):
    return negabinary_to_int(s[:-1]) * -2 + int(s) % 2 if s else 0

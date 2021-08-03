import re


def is_digit(n):
    print(n)
    return True if re.fullmatch(r"\d", n) else False

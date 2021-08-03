import re


def is_digit(n):
    pat = r"[^0-9]"
    return False if re.search(pat, n) or n == "" or int(n) > 9 else True

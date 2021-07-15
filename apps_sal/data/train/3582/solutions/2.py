import re
def is_digit(n):
    return bool(re.fullmatch(r'\d', n))

import re
def is_digit(n):
    return bool(re.findall(r"^\d{1}\Z", n))

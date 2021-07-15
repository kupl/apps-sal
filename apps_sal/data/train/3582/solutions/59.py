import re
def is_digit(n):
    if re.fullmatch("^[0-9]$", n):
        return True
    else:
        return False

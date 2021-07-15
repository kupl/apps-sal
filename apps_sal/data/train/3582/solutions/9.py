import re
def is_digit(n):
    if len(n) == 1 and re.match(r'^\d$', n):
        return True
    return False

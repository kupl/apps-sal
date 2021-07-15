import re
def is_digit(n):
    if len(n) > 1: return False
    digit = re.search('^\d$', n)
    return True if digit else False


import re
def is_digit(n):
    return True if re.search(r'[0-9]', n) != None and len(n) == 1 else False


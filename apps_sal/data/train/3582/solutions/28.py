import re
def is_digit(n):
    return bool(re.match(r'^[0-9]{1}\Z',n))

import re


def validate_code(c):
    return bool(re.search('^[1-3]', str(c)))

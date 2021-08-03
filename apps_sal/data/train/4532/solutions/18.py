import re


def validate_code(code):
    # your code here
    return bool(re.match(r'[1-3]', str(code)))

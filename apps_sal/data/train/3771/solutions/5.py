import re

VALID_NUM = re.compile(r'(\+44|0)7\d{9}$')


def validate_number(s):
    return "In with a chance" if VALID_NUM.match(s.replace("-", "")) else "Plenty more fish in the sea"

import re


def validate(s):
    return bool(re.match('MDZHB \\d\\d \\d{3} [A-Z]+( \\d\\d){4}$', s))

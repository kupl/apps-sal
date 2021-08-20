import re


def validate(message):
    return bool(re.match('MDZHB \\d\\d \\d\\d\\d [A-Z]+( \\d\\d){4}$', message))

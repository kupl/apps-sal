import re


def validate_pin(pin):
    """\\d only digits
    {} = number of digits with \\d
    | = or
    so, saying "accept all 4 or 6 elements if the're just digits"""
    if re.fullmatch('\\d{4}|\\d{6}', pin):
        return True
    else:
        return False

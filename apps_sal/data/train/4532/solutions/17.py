import re


def validate_code(code):
    if re.search('(\\A1)|(\\A2)|(\\A3)', str(code)):
        return True
    return False

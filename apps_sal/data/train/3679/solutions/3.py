import re


def calculate_string(st):
    return str(round(eval(re.sub(r'[^0-9\-\+\*\/\.]', "", st))))

import re


def seven_ate9(str_):
    return re.sub(r'79(?=7)', r'7', str_)

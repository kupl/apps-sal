import re


def seven_ate9(str):
    return re.sub('79(?=7)', '7', str)

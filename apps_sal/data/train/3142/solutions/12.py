import re


def seven_ate9(str_):
    return re.sub('79(?=7)', '7', str_)

import re


def seven_ate9(str_):
    pattern = '(?<=7)9(?=7)'
    return re.sub(pattern, '', str_)

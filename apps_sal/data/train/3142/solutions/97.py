import re


def seven_ate9(str_):
    return re.sub('(7)9(?=7)', '\\1', str_)

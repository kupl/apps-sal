import re


def seven_ate9(str_):
    if '797' not in str_:
        return str_
    return seven_ate9(re.sub('7(9)7', '77', str_))


import re

REGEXP = re.compile(r'79(?=7)')


def seven_ate9(str_):
    return REGEXP.sub('7', str_)


def seven_ate9(str_):
    while '797' in str_:
        str_ = str_.replace('797', '77')
    return str_

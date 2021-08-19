import re


def seven_ate9(str_):
    while str_ != re.sub('79+7', '77', str_):
        str_ = re.sub('797', '77', str_)
    return str_

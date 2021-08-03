import re


def seven_ate9(str_):
    while(str_ != re.sub(r'79+7', r'77', str_)):
        str_ = re.sub(r'797', r'77', str_)
    return str_

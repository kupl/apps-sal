import re


def replace_dots(str):
    return str.translate(str.maketrans('.', '-'))
    return str.replace('.', '-')
    return re.sub('\\.', '-', str)

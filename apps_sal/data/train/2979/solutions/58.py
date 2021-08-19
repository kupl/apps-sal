import re


def get_age(age):
    a = re.findall('\\d', age)
    a = ''.join(a)
    return int(a)

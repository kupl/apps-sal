import re


def get_age(age):
    a = re.findall(r'\d', age)
    a = ''.join(a)
    return int(a)

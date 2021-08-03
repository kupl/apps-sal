import re


def get_age(age):
    num = re.search('^(?P<age>\d+)\s', age)
    return int(num.group('age'))

import re


def get_age(age):
    return int(re.search('\\d+', age).group())

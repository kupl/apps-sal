import re


def get_age(age):
    pattern = re.compile('[0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9]+')
    return int(re.findall(pattern, age)[0])

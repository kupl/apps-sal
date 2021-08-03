import re


def get_age(age):
    for element in re.findall('[0-9]', age):
        return int(element)

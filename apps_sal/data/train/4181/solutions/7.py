import re


def filter_numbers(string):
    return re.sub('\d', '', string)

import re


def dad_filter(string):
    return re.sub(r',+', r',', string).rstrip(', ')

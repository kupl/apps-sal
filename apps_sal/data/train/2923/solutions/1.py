import re


def dad_filter(string):
    return re.sub(',+', ',', string).rstrip(', ')

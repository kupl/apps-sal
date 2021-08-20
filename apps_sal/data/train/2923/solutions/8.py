import re


def dad_filter(string):
    string = re.sub(',+', ',', string.strip())
    if string[-1] == ',':
        return string[:-1]
    else:
        return string

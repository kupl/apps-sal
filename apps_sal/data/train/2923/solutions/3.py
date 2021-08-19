import re


def dad_filter(string):
    return re.sub(',* *$', '', re.sub(',{2,}', ',', string))

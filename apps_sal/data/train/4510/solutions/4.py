import re


def to_underscore(string):
    try:
        return '_'.join(x.lower() for x in re.findall('[A-Z][^A-Z]*', string))
    except:
        return str(string)

import re


def string_parse(s):
    try:
        return re.sub('(.)\\1+', lambda m: m.group()[0:2] + '[' + m.group()[2:] + ']' if len(m.group()) > 2 else m.group(), s)
    except TypeError:
        return 'Please enter a valid string'

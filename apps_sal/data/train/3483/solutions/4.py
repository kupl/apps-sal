import re


def string_parse(string):
    try:

        def replace(match):
            return '{0}{0}[{1}]'.format(*match.group(1, 2))
        return re.sub('(.)\\1(\\1+)', replace, string)
    except TypeError:
        return 'Please enter a valid string'

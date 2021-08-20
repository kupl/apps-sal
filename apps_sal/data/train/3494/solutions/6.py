import re


def pig_it(text):
    return re.sub('(\\w{1})(\\w*)', '\\2\\1ay', text)

import re


def replace_dots(str):
    compiler = re.compile('\\.')
    return compiler.sub('-', str)

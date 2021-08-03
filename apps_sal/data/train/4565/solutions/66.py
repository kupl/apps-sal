import re


def replace_dots(str):
    compiler = re.compile(r'\.')
    return compiler.sub("-", str)

import re

def camelize(s):
    return "".join(map(str.capitalize, re.split("\W|_", s)))

import re


def camelize(str_):
    words = re.findall(r'[a-z0-9]+', str_, flags=re.I)
    return ''.join(word.capitalize() for word in words)

import re


def rad_ladies(name):
    return ''.join(re.findall('[a-zA-Z !]', name)).upper()

import re


def rad_ladies(name):
    return re.sub(r'[\d%$&/£?@]', r'', name).upper()

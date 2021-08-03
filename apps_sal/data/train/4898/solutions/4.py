import re


def digit_all(x):
    if not isinstance(x, str):
        return 'Invalid input !'
    regex = re.compile(r'[^0-9]')
    return re.sub(regex, '', x)

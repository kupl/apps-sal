import re


def increment_string(string):
    digits = re.search('\\d+$', string)
    if not len(string):
        return '{}'.format('1')
    elif digits:
        return '{}{}'.format(string.replace(digits.group(), ''), str(int(digits.group()) + 1).zfill(len(digits.group())))
    else:
        return '{}{}'.format(string, '1')

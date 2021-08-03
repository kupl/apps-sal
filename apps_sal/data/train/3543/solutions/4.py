import re


def increment_string(strng):
    m = re.match('^(.*?)(\d+)$', strng)
    name, num = (m.group(1), m.group(2)) if m else (strng, '0')
    return '{0}{1:0{2}}'.format(name, int(num) + 1, len(num))

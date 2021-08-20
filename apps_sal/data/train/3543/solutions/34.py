import re


def increment_string(strng):
    m = re.match('^(.*?)(\\d*)$', strng)
    (word, digits) = (m.group(1), m.group(2))
    if digits:
        digits = str(int(digits) + 1).zfill(len(digits))
    else:
        digits = '1'
    return word + digits

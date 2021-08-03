import re


def increment_string(strng):
    m = re.split(r"(\d+)", strng)
    if len(m) < 2:
        return strng + "1"
    else:
        number = str(int(m[-2]) + 1).zfill(len(m[-2]))
        return ''.join(m[0:-2]) + number

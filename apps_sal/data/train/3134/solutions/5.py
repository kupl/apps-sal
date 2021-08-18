import re


def is_valid(idn):
    line = re.match(r'[a-zA-Z_$]\w*$', idn)
    if line:
        return True
    else:
        return False

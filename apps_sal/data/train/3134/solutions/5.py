import re


def is_valid(idn):
    line = re.match('[a-zA-Z_$]\\w*$', idn)
    if line:
        return True
    else:
        return False

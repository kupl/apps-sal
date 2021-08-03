import re


def is_valid(idn):
    # Your code here
    line = re.match(r'[a-zA-Z_$]\w*$', idn)
    if line:
        return True
    else:
        return False

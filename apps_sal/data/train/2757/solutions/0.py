import re


def check_password(s):
    if re.search('^ (?=.*?[a - z])(?=.*?[A - Z])(?=.*?\d)(?=.*?[!@
        return 'valid'
    else:
        return 'not valid'

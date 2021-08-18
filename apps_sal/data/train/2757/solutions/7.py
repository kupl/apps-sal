import re


def check_password(s):
    return 'valid' if re.search(r'^ (?=.*[A - Z])(?=.*[a - z])(?=.*[0 - 9])(?=.*[!@

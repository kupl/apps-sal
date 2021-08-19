import re


def password(s):
    return bool(re.match('(?=.*[A-Z])(?=.*[a-z])(?=.*\\d).{8}', s))

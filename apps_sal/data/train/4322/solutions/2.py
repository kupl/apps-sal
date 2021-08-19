import re


def body_count(s):
    return bool(re.search('([A-Z]\\d){5}\\.-[A-Z]%\\d\\.\\d\\d\\.', s))

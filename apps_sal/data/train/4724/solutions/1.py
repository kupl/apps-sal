import re


def drop_cap(s):
    return re.sub(r'\w{3,}', lambda m: m[0].title(), s)

import re


def drop_cap(s):
    return re.sub('\\S{3,}', lambda m: m.group(0).title(), s)

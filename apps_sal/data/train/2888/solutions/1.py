from re import sub


def remove(s):
    return sub('(\\w+)!+(\\s+|$)', '\\1\\2', s)

from re import sub


def reverse(string):
    return sub('(\\w)\\1+', lambda m: m.group().swapcase(), string)

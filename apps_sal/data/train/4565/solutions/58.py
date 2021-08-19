from re import sub


def replace_dots(string):
    return sub('\\.', '-', string)

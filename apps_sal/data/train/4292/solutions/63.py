import string


def string_clean(s):
    out = ''
    for element in s:
        if not element.isnumeric():
            out += element
    return out

import string


def string_clean(s):
    for n in s:
        if n in string.digits:
            s = s.replace(n, '')
    return s

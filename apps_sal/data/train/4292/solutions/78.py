from string import digits


def string_clean(s):
    for char in digits:
        s = s.replace(char, '')
    return s

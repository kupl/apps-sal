from string import digits


def string_clean(s):
    foo = str.maketrans('', '', digits)
    bar = s.translate(foo)
    return bar

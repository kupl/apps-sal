def string_clean(s):
    return ''.join(__import__('itertools').filterfalse(str.isdigit, s))

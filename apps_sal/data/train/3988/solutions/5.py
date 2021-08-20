from re import sub


def encode(s):
    return sub('(.)\\1*', lambda m: str(len(m.group(0))) + m.group(1), s)


def decode(s):
    return sub('(\\d+)(\\D)', lambda m: m.group(2) * int(m.group(1)), s)

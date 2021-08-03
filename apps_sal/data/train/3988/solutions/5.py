from re import sub


def encode(s):
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)


def decode(s):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), s)

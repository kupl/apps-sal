def remove_char(s):
    long = len(s)
    s = s[:0] + s[(0 + 1):]
    s = s[:long - 2] + s[(long - 1):]
    return s

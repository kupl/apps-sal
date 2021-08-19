def string_transformer(s):
    s = s.swapcase()
    s = s.split(' ')[::-1]
    s = ' '.join(s)
    return s

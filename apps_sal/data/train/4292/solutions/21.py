def string_clean(s):
    return s.translate({ord(x): None for x in '0123456789'})

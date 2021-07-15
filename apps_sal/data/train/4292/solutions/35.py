def string_clean(s):
    return ''.join('' if ch in "0123456789" else ch for ch in list(s))

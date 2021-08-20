def string_clean(s):
    return ''.join((ch for ch in s if ch not in '0123456789'))

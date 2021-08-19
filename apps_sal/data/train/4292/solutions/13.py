def string_clean(s):
    return ''.join((c for c in s if c not in '1234567890'))

def string_clean(s):
    return ''.join((c for c in s if not c.isdigit()))

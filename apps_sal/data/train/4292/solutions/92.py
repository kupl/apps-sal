def string_clean(s):
    str = ''
    return str.join((c for c in s if not c.isdigit()))

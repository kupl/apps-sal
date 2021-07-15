def string_clean(s):
    return ''.join(list(el if not el.isdigit() else '' for el in s))

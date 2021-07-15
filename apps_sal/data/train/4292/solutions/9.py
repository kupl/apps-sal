def string_clean(s):
    return ''.join([item for item in s if not item.isdigit()])

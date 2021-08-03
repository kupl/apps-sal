def string_clean(s):
    import re
    return ''.join(re.findall('\D', s))

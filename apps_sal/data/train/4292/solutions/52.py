def string_clean(s):
    return ''.join([s[x] for x in range(len(s)) if not s[x].isnumeric()])

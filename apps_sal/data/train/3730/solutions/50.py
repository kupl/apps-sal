def capitalize(s):
    return [''.join([v.upper() if i % 2 == 0 else v for (i, v) in enumerate(s)]), ''.join([v.upper() if i % 2 == 1 else v for (i, v) in enumerate(s)])]

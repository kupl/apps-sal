def capitalize(s):
    return [''.join((x if i % 2 else x.upper() for (i, x) in enumerate(s))), ''.join((x.upper() if i % 2 else x for (i, x) in enumerate(s)))]

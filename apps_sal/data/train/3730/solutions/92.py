def capitalize(s):
    return [''.join([c if k % 2 else c.upper() for k, c in enumerate(s)]), ''.join([c.upper() if k % 2 else c for k, c in enumerate(s)])]

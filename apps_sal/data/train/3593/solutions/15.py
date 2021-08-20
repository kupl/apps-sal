def capitalize(s, a):
    return ''.join(((x, x.upper())[y in a] for (y, x) in enumerate(s)))

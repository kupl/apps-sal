def find_children(s):
    return ''.join(sorted(s, key=lambda c: (c.lower(), c)))

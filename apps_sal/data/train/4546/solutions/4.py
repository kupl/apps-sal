def find_children(dancing_brigade):
    return ''.join(sorted(dancing_brigade, key=lambda c: (c.lower(), c.islower())))

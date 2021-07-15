def find_children(a):
    return ''.join(sorted(a, key=lambda s: (s.upper(), s.islower())))

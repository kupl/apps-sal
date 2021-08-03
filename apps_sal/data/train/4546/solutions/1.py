def find_children(s):
    return ''.join(sorted(sorted(s), key=str.lower))

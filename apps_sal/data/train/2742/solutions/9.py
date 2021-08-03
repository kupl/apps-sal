def scramble(a, b):
    if not a or not b:
        return ''
    if len(a) != len(b):
        return ''
    s = sorted(zip(b, a))
    a, b = map(list, zip(*s))
    return ''.join(b)

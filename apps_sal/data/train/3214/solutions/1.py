def change(s):
    s = set(s.lower())
    return ''.join(('1' if x in s else '0' for x in map(chr, range(97, 123))))

def ones_complement(s):
    return ''.join(({'0': '1'}.get(c, '0') for c in s))

def sort_string(s):
    it = iter(sorted(filter(str.isalpha, s), key=str.lower))
    return ''.join(next(it) if c.isalpha() else c for c in s)

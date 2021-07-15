def sort_string(s):
    a = iter(sorted((c for c in s if c.isalpha()), key=str.lower))
    return ''.join(next(a) if c.isalpha() else c for c in s)

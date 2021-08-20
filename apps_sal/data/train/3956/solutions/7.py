def sort_string(s):
    it = iter(sorted([(i, x) for (i, x) in enumerate(s) if x.isalpha()], key=lambda p: (p[1].lower(), p[0])))
    return ''.join((next(it)[1] if x.isalpha() else x for x in s))

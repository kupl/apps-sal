def sort_string(s):
    alphas = [x for x in s if x.isalpha()]
    res = iter(sorted(alphas, key=lambda x: x.lower()))
    return ''.join((next(res) if x.isalpha() else x for x in s))

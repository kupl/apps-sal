def sort_string(s):
    a = iter(sorted(filter(str.isalpha, s), key=str.lower))
    return "".join(next(a) if x.isalpha() else x for x in s)

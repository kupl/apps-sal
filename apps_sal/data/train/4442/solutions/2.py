def case_sensitive(s):
    l = list(filter(str.isupper, s))
    return [not l, l]

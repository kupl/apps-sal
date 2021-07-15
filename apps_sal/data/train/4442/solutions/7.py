def case_sensitive(s):
    res = list(filter(str.isupper, s))
    return [not res, res]

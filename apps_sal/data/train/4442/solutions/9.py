def case_sensitive(s):
    uppers = [c for c in s if c.isupper()]
    return [not uppers, uppers]

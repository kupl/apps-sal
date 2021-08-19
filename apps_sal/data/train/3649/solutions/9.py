def aa_percentage(s, a=None):
    print(repr(a))
    return round(100 * sum((i in ('AILMFWYV' if a is None else a) for i in s)) / len(s))

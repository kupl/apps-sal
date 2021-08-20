def drop_cap(s):
    return ' '.join((x.title() if len(x) > 2 else x for x in s.split(' ')))

def the_biggest_search_keys(*args):
    by_len = {}
    fmt = "'{}'".format
    for a in args:
        by_len.setdefault(len(a), []).append(a)
    try:
        return ', '.join(fmt(b) for b in sorted(by_len[max(by_len)]))
    except ValueError:
        return "''"


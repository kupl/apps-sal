def the_biggest_search_keys(*args):
    maxLen = max(map(len, args), default=None)
    return "''" if not args else ", ".join(sorted(filter(lambda s: len(s) - 2 == maxLen, map(lambda s: "'{}'".format(s), args))))

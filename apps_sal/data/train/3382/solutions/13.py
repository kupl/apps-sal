def lowercase_count(s):
    return len(list(filter(lambda x: x in map(chr, range(97, 123)), s)))

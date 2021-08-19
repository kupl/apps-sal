def only_duplicates(string):
    sets = (unique, duplicate) = (set(), set())
    for c in string:
        sets[c in unique].add(c)
    return ''.join((c for c in string if c in duplicate))

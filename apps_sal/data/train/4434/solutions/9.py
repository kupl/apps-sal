def first_non_repeated(s):
    sets = unique, repeated = set(), set()
    for c in s:
        sets[c in unique].add(c)
    return next((c for c in s if c not in repeated), None)

def relations(family, pair):
    if pair in family:
        return "Daughter"
    if pair[::-1] in family:
        return "Mother"

    asc = {d: m for m, d in family}
    mother = asc.get
    if mother(mother(pair[0])) == pair[1]:
        return "Grandmother"
    if mother(mother(pair[1])) == pair[0]:
        return "Granddaughter"

    desc = {}
    for m, d in family:
        desc.setdefault(m, []).append(d)

    def is_sister(a, b): return not all({a, b} - set(gen) for gen in list(desc.values()))
    if is_sister(*pair):
        return "Sister"
    if is_sister(mother(pair[0]), pair[1]):
        return "Aunt"
    if is_sister(mother(pair[1]), pair[0]):
        return "Niece"

    return "Cousin"

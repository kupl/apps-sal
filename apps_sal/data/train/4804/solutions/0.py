def relations(family_list, target_pair):
    parents = {}
    for parent, child in family_list:
        parents[child] = parent

    a, b = target_pair
    ap = parents.get(a)
    app = parents.get(ap)
    bp = parents.get(b)
    bpp = parents.get(bp)

    if b == ap:
        return 'Mother'
    if b == app:
        return 'Grandmother'
    if a == bp:
        return 'Daughter'
    if a == bpp:
        return 'Granddaughter'
    if ap == bp:
        return 'Sister'
    if app == bpp:
        return 'Cousin'
    if app == bp:
        return 'Aunt'
    if ap == bpp:
        return 'Niece'

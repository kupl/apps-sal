def relations(family, target):
    parents = {}
    for parent, child in family:
        parents[child] = parent
    a, b = target
    ap = parents.get(a)
    app = parents.get(ap)
    bp = parents.get(b)
    bpp = parents.get(bp)
    if b == ap:
        return "Mother"
    elif b == app:
        return "Grandmother"
    elif a == bp:
        return "Daughter"
    elif a == bpp:
        return "Granddaughter"
    elif ap == bp:
        return "Sister"
    elif app == bpp:
        return "Cousin"
    elif app == bp:
        return "Aunt"
    elif ap == bpp:
        return "Niece"

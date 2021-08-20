def poly_add(p1, p2):
    (s, l) = sorted([p1, p2], key=lambda p: len(p))
    x = [sum(f) for f in zip(s, l)]
    x.extend(l[len(s):])
    return x

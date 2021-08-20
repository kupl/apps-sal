def atomic_number(e):
    (l, shells) = (1, [])
    while e:
        n = min(2 * l * l, e)
        shells.append(n)
        (e, l) = (e - n, l + 1)
    return shells

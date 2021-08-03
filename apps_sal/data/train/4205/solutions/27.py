def cannons_ready(g):
    x = "Fire!"
    y = "Shiver me timbers!"

    for b in g.values():
        if b == 'nay':
            return y
    return x

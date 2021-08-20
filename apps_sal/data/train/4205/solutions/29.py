def cannons_ready(g):
    return 'Fire!' if len(g) == tuple(g.values()).count('aye') else 'Shiver me timbers!'

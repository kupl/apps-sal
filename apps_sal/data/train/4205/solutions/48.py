def cannons_ready(g):
    return 'Fire!' if all(g[i] == 'aye' for i in g) else  'Shiver me timbers!'

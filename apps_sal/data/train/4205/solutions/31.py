def cannons_ready(g):
    return 'Shiver me timbers!' if any((g[x] == 'nay' for x in g)) else 'Fire!'

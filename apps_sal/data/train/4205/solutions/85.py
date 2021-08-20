def cannons_ready(g):
    return 'Fire!' if all((x == 'aye' for x in g.values())) else 'Shiver me timbers!'

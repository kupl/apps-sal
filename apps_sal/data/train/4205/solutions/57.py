def cannons_ready(g):
    for i in g.values():
        if i != 'aye':
            return 'Shiver me timbers!'
    return 'Fire!'

def cannons_ready(g):
    return ['Shiver me timbers!', 'Fire!'][all(i=='aye' for i in g.values())]

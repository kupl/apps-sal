def cannons_ready(d):
    return 'Fire!' if len(set(d.values())) == 1 else 'Shiver me timbers!'

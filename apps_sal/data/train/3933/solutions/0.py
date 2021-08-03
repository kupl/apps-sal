def hydrate(drink_string):
    c = sum(int(c) for c in drink_string if c.isdigit())
    return "{} {} of water".format(c, 'glass') if c == 1 else "{} {} of water".format(c, 'glasses')

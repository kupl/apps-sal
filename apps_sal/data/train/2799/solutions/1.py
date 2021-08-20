def beasts(h, t):
    out = [(5 * t - h) / 3, (h - 2 * t) / 3]
    return all((x.is_integer() and x >= 0 for x in out)) and out or 'No solutions'

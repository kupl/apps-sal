def animals(h, l):
    return (2 * h - 1 / 2 * l, -h + 1 / 2 * l) if (2 * h - 1 / 2 * l).is_integer() and (-h + 1 / 2 * l).is_integer() and (2 * h - 1 / 2 * l) >= 0 and (-h + 1 / 2 * l) >= 0 else 'No solutions'

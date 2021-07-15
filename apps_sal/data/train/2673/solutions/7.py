def passer_rating(att, yds, comp, td, ints):
    A = max(min(2.375, ((comp / att) - .3) * 5), 0)
    B = max(min(2.375, ((yds / att) - 3) * .25), 0)
    C = max(min(2.375, (td / att) * 20), 0)
    D = max(min(2.375, 2.375 - ((ints / att) * 25)), 0)
    return round(((A + B + C + D) / 6) * 100, 1)


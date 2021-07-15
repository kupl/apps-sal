def passer_rating(att, yds, comp, td, ints):
    a = ((comp / att) - 0.3) * 5
    b = ((yds / att) - 3) * 0.25
    c = (td / att) * 20
    d = 2.375 - ((ints / att) * 25)
    return round(sum(max(0, min(x, 2.375)) for x in [a, b, c, d]) * 50 / 3, 1)

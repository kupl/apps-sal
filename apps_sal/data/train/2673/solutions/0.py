def passer_rating(att, yds, comp, td, ints):
    def limit(x): return min(max(x, 0), 2.375)

    att = float(att)

    A = ((comp / att) - .3) * 5
    B = ((yds / att) - 3) * .25
    C = (td / att) * 20
    D = 2.375 - ((ints / att) * 25)

    A, B, C, D = map(limit, (A, B, C, D))

    return round((A + B + C + D) / 6 * 100, 1)

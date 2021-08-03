def passer_rating(att, yds, comp, td, ints):
    def cap(x): return max(0, min(x, 2.375))
    a = cap(((comp / att) - 0.3) * 5)
    b = cap(((yds / att) - 3) * 0.25)
    c = cap((td / att) * 20)
    d = cap(2.375 - ((ints / att) * 25))
    return round((a + b + c + d) / 6 * 100, 1)

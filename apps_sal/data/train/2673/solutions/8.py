def passer_rating(att, yds, comp, td, ints):
    return round(sum(map(lambda n: min(2.375, max(0, n)), [(comp / att - 0.3) * 5, (yds / att - 3) * 0.25, td / att * 20, 2.375 - ints / att * 25])) / 6 * 100, 1)

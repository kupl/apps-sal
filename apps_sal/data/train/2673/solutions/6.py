def passer_rating(att, yds, comp, td, ints):

    def bording(score):
        if score < 0:
            return 0
        if score > 2.375:
            return 2.375
        return score
    a = bording((comp / att - 0.3) * 5)
    b = bording((yds / att - 3) * 0.25)
    c = bording(td / att * 20)
    d = bording(2.375 - ints / att * 25)
    return round((a + b + c + d) / 6 * 100, 1)

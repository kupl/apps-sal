def passer_rating(att, yds, comp, td, ints):
    A = (comp / att - 0.3) * 5
    B = (yds / att - 3) * 0.25
    C = td / att * 20
    D = 2.375 - ints / att * 25
    lst = [2.375 if element > 2.375 else 0 if element < 0 else element for element in (A, B, C, D)]
    passer_rating = sum(lst) / 6 * 100
    return round(passer_rating, 1)

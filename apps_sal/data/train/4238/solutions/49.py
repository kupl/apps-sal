def squares_needed(grains):

    def sum_of_squares(sqr):
        return ((2**(sqr)) - 1) / (2 - 1)

    sqr = 0
    while True:
        if sum_of_squares(sqr) >= grains:
            return sqr
            break
        sqr += 1

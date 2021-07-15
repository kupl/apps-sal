def make_negative( number ):
    if number < 0:
        return number
    elif number == 0:
        return 0
    else:
        neg = number - 2 * number
        return neg

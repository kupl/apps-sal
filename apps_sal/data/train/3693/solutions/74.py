def make_negative( number ):
    if number == 0:
        return 0
    if number < 0:
        return number
    else:
        return number - 2*number

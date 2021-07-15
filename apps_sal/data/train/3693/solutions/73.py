def make_negative( number ):
    if number == 0:
        return 0
    elif number > 0:
        number *= -1
        return number
    elif number < 0:
        return number

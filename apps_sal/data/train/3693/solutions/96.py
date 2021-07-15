def make_negative( number ):
    if number <= 0:
        return number
    elif number > 0:
        number -= number * 2
        return number


def make_negative( number ):
    if number > 0:
        number = '-' + str(number)  ;
        return int(number)
    elif number == 0:
        return 0
    else:
        return number

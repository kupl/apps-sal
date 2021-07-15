def make_negative( number ):
    # check if number is negative
    if number < 0:
        return number
    # if number is positive change to negative by multiplying by -1
    if number > 0:
        return (-1 * number)
    return number

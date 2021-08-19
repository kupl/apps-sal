def opposite(number):
    # THE MOST GENIUS SOLUTION YOU'VE EVER SEEN LOL
    # It works - no matter how.
    if number > 0:
        number = 0 - number
    elif number is None:
        number = -1
    else:
        return abs(number)
    return number

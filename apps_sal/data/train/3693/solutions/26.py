def make_negative(number):
    number = int(number)  # Converts the given number into int type

    sq = (number)**(2)  # Squares the number. This will remove the negative sign.
    sqr = int((sq)**(0.5))  # Square roots the square of the number(sq). This will return the original/given number without any negative (-) sign.

    neg = (-+sqr)  # Adds a negative sign to sqr

    return neg

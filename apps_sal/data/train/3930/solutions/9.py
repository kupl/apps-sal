
def dollar_to_speech(value):
    pass

    if "-" in value:

        return 'No negative numbers are allowed!'

    else:

        d = int(value[1::].split('.')[0])

        c = int(value[1::].split('.')[1])

        if d == 0 and c == 0:

            return "0 dollars."

        if d == 1 and c == 0:

            return "{} dollar.".format(d)

        if d > 1 and c == 0:

            return "{} dollars.".format(d)

        if d == 0 and c == 1:

            return "{} cent.".format(c)

        if d == 0 and c > 1:

            return "{} cents.".format(c)

        if d == 1:

            m = 'dollar'

        if d > 1:

            m = 'dollars'

        if c == 1:

            k = 'cent'

        if c > 1:

            k = 'cents'

        if d > 0 and c > 0:

            return "{} {} and {} {}.".format(d, m, c, k)

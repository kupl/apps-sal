def isDigit(string):
    truth = False

    try:
        if type((int(string))) is int:
            truth = True
    except ValueError:
        truth = False

    try:
        if type(float(string)):
            truth = True
    except ValueError:
        truth = False

    return truth

def next_num(n):
    '''
    I work on input number converting it to string throughout the code.
    We check if number is polydivisible, if not we find where in the number 
    first problem occurs and then substitute proper part into the initial 
    number and check over again.
    '''
    number = str(n + 1)

    def isNumPoly(number):
        for i in range(1, len(number) + 1):
            if not (int(number[0:i])) % (i) == 0:
                return i
        return 0
    while (int(number) < 3610000000000000000000000):
        where = isNumPoly(number)
        if where == 0:
            return int(number)
        badPiece = number[0:where]
        replacement = str(int(badPiece) + (where - int(badPiece) % where))
        number = replacement + "0" * len(number[where:])
    return None

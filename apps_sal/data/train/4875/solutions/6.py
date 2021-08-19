def is_valid_coordinates(coordinates):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    dec = '.'
    comma = ','
    space = ' '
    neg = '-'
    (negOK, digitOK) = (True, True)
    (decOK, spaceOK, commaOK) = (False, False, False)
    hitComma = False
    hitDec = False
    for c in coordinates:
        print(c)
        if hitComma:
            commaOK = False
        if c in digits:
            if not digitOK:
                return False
            if not hitDec:
                decOK = True
            commaOK = True
            negOK = False
            continue
        elif c == neg:
            if not negOK:
                return False
            (negOK, commaOK, decOK, spaceOK) = (False, False, False, False)
            continue
        elif c == dec:
            if not decOK:
                return False
            (negOK, commaOK, decOK, spaceOK) = (False, False, False, False)
            digitOK = True
            hitDec = True
            continue
        elif c == comma:
            if not commaOK:
                return False
            (negOK, commaOK, decOK, digitOK) = (False, False, False, False)
            spaceOK = True
            continue
        elif c == space:
            if not spaceOK:
                return False
            (negOK, digitOK) = (True, True)
            (decOK, spaceOK, commaOK) = (False, False, False)
            hitComma = True
            hitDec = False
            continue
        return False
    cArr = coordinates.split(', ')
    if abs(float(cArr[0])) > 90 or abs(float(cArr[1])) > 180:
        return False
    return True

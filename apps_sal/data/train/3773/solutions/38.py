def isValid(formula):
    print(formula)
    f = list(map(str, formula))
    f1 = str(''.join(f))
    b = 0
    if f1.find('7') != -1:
        for i in f1:
            b = i
            if b == '1':
                if f1.find('2') == -1:
                    continue
                else:
                    return False
            elif b == '3':
                if f1.find('4') == -1:
                    continue
                else:
                    return False
            elif b == '5':
                if f1.find('6') != -1:
                    return True
                else:
                    return False
            elif b == '6':
                if f1.find('5') != -1:
                    return True
                else:
                    return False
    elif f1.find('8') != -1:
        for i in f1:
            b = i
            if b == '1':
                if f1.find('2') == -1:
                    continue
                else:
                    return False
            elif b == '3':
                if f1.find('4') == -1:
                    continue
                else:
                    return False
            elif b == '5':
                if f1.find('6') != -1:
                    return True
                else:
                    return False
            elif b == '6':
                if f1.find('5') != -1:
                    return True
                else:
                    return False
    else:
        return False
    return True

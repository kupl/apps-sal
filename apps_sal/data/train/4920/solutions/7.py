def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def lcd(a, b):
    return a * b / gcd(a, b)


def checkstring(arr):
    strlist = []
    for elem in arr:
        if type(elem) == str:
            strlist.append(elem)
    return strlist


def converttoint(arr):
    intarray = []
    for elem in arr:
        if elem is None:
            pass
        else:
            try:
                intarray.append(int(elem))
            except:
                intarray.append(elem)
    return intarray


def min_special_mult(arr):
    arr = converttoint(arr)
    if len(checkstring(arr)) == 1:
        return 'There is 1 invalid entry: ' + str(checkstring(arr)[0])
    elif len(checkstring(arr)) > 1:
        return 'There are ' + str(len(checkstring(arr))) + ' invalid entries: ' + str(checkstring(arr))
    current = 1
    for elem in arr:
        current = lcd(current, elem)
    return current

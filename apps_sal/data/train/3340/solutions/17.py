import math


def sharkovsky(a, b):
    if a % 2 != b % 2:
        if b == 1:
            return True
        elif (a % 2 == 1) & (a != 1):
            return True
        else:
            return False
    elif a % 2 == 1:
        if b == 1:
            return True
        elif (a < b) & (a != 1):
            return True
        else:
            return False
    elif (math.pow(2, int(math.log2(a))) == a) & (math.pow(2, int(math.log2(b))) == b) & (a > b):
        return True
    elif math.pow(2, int(math.log2(a))) != a:
        if math.pow(2, int(math.log2(b))) == b:
            return True
        else:
            i = 0
            while a % 2 == 0 and b % 2 == 0:
                i += 1
                a = a / 2
                b = b / 2
            if b % 2 == 0:
                return True
            elif a % 2 == 0:
                return False
            elif a < b:
                return True
            else:
                return False
    else:
        return False

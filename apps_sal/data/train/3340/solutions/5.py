def sharkovsky(a, b):
    if b == a:
        return False
    elif b == 1:
        return True
    elif a == 1:
        return False
    elif a%2 == 1:
        if b%2 == 0:
            return True
        elif a<b:
            return True
        else:
            return False
    else:
        if b%2 == 1:
            return False
        else:
            result = sharkovsky(a/2, b/2)
            return result

def feast(beast, dish):
    a = beast[0]
    b = beast[-1]
    c = dish[0]
    d = dish[-1]
    if a == c:
        if b == d:
            return True
        else:
            return False
    elif a != c:
        return False

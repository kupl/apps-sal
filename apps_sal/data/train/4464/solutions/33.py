def feast(beast, dish):
    a = beast[0]
    b = beast[len(beast)-1]
    c = dish[0]
    d = dish[len(dish)-1]
    if a.lower() == c.lower() and b.lower() == d.lower():
        return True
    else:
        return False


def feast(beast, dish):
    first = beast[0]
    last = beast[-1]
    first1 = dish[0]
    last1 = dish[-1]
    if first == first1 and last == last1:
        return True
    else:
        return False

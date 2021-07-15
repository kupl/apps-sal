def feast(beast, dish):
    print(beast[1])
    print(beast[-1])
    print(dish[1])
    print(dish[-1])
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False

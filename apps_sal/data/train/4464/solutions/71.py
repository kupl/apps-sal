def feast(beast, dish):
    print(beast, dish)
    return True if beast[-1] == dish[-1] and beast[0] == dish[0]else False

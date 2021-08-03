def feast(beast, dish):
    # if beast[0] == dish[0] and beast[last index] == dish[last index] return True
    return beast[0] == dish[0] and beast[-1] == dish[-1]

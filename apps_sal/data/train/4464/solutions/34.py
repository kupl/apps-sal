def feast(beast, dish):
    return beast[0:1] == dish[0:1] and beast[::-1][0:1] == dish[::-1][0:1]

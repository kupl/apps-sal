def feast(beast, dish):
    return True if beast[0]==dish[0] and beast[::-1][0]==dish[::-1][0] else False

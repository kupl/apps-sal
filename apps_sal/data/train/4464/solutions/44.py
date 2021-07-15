def feast(beast, dish):
    for char in beast:
        if beast[0] == dish[0] and beast[-1] == dish[-1]:
            return True
        else:
            return False

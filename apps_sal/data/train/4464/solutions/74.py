def feast(beast, dish):
    for i in beast:
        if beast[0] == dish[0]:
            if beast[-1] == dish[-1]:
                return True
            else:
                return False
        else:
            return False

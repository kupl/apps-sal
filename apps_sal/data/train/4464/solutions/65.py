def feast(beast, dish):
    return True if beast.split()[0][0] == dish.split()[0][0] and beast.split()[-1][-1] == dish.split()[-1][-1] else False

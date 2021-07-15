def find_unknown_number(x,y,z):
    return min(set(range(x or 3, 106, 3)) & set(range(y or 5, 106, 5)) & set(range(z or 7, 106, 7)))

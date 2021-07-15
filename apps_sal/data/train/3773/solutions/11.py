def isValid(f):
    if 1 in f and 2 in f:
        return False
    else:
        if 3 in f and 4 in f:
            return False
        else:
            if 5 in f and 6 in f:
                if 7 in f or 8 in f:
                    return True
                else:
                    return False
            else:
                if 5 in f or 6 in f:
                    return False
                else:
                    if 7 in f or 8 in f:
                        return True
                    else:
                        return False

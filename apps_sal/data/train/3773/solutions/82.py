def isValid(f):
    if 5 in f or 6 in f:
        if not (5 in f and 6 in f):
            return False

    if not (7 in f or 8 in f):
        return False

    if 1 in f or 2 in f:
        if 1 in f and 2 in f:
            return False

    if 3 in f or 4 in f:
        if 3 in f and 4 in f:
            return False

    return True


print(isValid([1, 3, 7]))

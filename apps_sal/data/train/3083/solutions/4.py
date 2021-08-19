def polydivisible(x):
    if x < 10:
        return True
    return not x % len(str(x)) and polydivisible(int(str(x)[:-1]))

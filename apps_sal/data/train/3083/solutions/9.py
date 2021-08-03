def polydivisible(x):
    li = list(str(x))
    for i, digit in enumerate(li):
        if int("".join(li[:i + 1])) % (i + 1) != 0:
            return False
    return True

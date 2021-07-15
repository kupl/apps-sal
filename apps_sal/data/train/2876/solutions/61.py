def check(a, x):
    if x == str(x):
        if str(x) in a:
            return True
        else:
            return False
    elif x == int(x):
        if int(x) in a:
            return True
    return False

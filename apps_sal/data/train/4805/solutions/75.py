def check(a, x):
    check = 0
    if a.count(x) <= 1:
        check = check + 1
    if check == 1:
        return (a.count(x))
    elif check <= 2:
        return True
    else:
        return (False)

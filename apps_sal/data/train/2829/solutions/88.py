def array_madness(a, b):
    lsta = []
    lstb = []
    for x in a:
        x = x ** 2
        lsta.append(x)
    for y in b:
        y = y ** 3
        lstb.append(y)
    if sum(lsta) >= sum(lstb):
        return True
    else:
        return False

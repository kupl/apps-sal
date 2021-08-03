def well(x):
    y = "good"
    count = 0
    cw = 0
    while len(x) > cw:
        if x[cw] == y:
            count = count + 1
            cw = cw + 1
        else:
            cw = cw + 1
    if count == 1 or count == 2:
        return "Publish!"
    elif count > 2:
        return "I smell a series!"
    else:
        return "Fail!"

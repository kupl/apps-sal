def mutually_exclusive(dice, call1, call2):
    checknull = 0
    diecall1 = 0
    diecall2 = 0
    for die in dice:
        checknull += die[1]
        if die[0] == call1:
            diecall1 = die[1]
        elif die[0] == call2:
            diecall2 = die[1]
    if checknull != 1:
        return None
    else:
        return format((diecall1 + diecall2), ".2f")

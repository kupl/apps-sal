def mutually_exclusive(dice, call1, call2):
    checknull = 0
    diecall1 = 0
    diecall2 = 0
    for die in dice:
        # [3,0.4]
        checknull += die[1]
        if die[0] == call1:
            diecall1 = die[1]
        elif die[0] == call2:
            diecall2 = die[1]
    if checknull != 1:
        return None
    else:
        return format((diecall1 + diecall2), ".2f")  # - (diecall1*diecall2),2)) #:[

#dice = [[3,0.4],[4,0.1],[1,0.01],[2,0.09],[5,0.2],[6,0.1]]

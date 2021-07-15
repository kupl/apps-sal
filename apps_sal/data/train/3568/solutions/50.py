def bumps( road ):
    cnt1, cnt2 = 0, 0
    for c in road:
        if c == "_":
            cnt1 += 1
        elif c == "n":
            cnt2 += 1
        if cnt2 > 15:
            return "Car Dead"
    return "Woohoo!"


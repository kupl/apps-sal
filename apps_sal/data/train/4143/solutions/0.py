def points(dice):
    dice = sorted([int(d) for d in dice])
    counts = [dice.count(i) for i in range(1, 7)]
    if 5 in counts:
        return 50
    if 4 in counts:
        return 40
    if 3 in counts and 2 in counts:
        return 30
    if counts.count(1) == 5 and counts.index(0) not in [2, 3, 4]:
        return 20
    return 0

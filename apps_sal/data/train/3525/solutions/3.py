def flipping_game(num):
    poss_start = [i for (i, x) in enumerate(num) if x == 0 and (i == 0 or num[i - 1] == 1)]
    poss_end = [i for (i, x) in enumerate(num) if x == 0 and (i == len(num) - 1 or num[i + 1] == 1)]
    if not poss_start or not poss_end:
        return sum(num) - 1
    curmax = 0
    for st in poss_start:
        for en in poss_end:
            curmax = max(curmax, sum((x if i < st or i > en else 1 - x for (i, x) in enumerate(num))))
    return curmax

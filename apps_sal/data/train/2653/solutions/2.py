def bingo(array):
    ctr = 0
    for i in [2, 9, 14, 7, 15]:
        if i in list(set(array)):
            ctr += 1
    if ctr == 5:
        return "WIN"
    else:
        return "LOSE"
    pass

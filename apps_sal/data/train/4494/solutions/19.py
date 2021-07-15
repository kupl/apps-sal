def points(games):
    pnts, lst = 0, [i for i in games]
    
    for j in range(len(lst)):
        if lst[j][0] > lst[j][2]:
            pnts += 3
        if lst[j][0] == lst[j][2]:
            pnts += 1

    return pnts

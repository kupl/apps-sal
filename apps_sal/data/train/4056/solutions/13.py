def leaderboard_sort(lb, chn):
    for name in chn:
        nm, diff = tuple(name.split())
        diff = int(diff)
        ind = lb.index(nm)
        if diff > 0:
            lb.insert(ind-diff, nm)
            lb.pop(ind+1)
        else:
            lb.insert(ind+abs(diff)+1, nm)
            lb.pop(ind)
    print(lb)
    return lb

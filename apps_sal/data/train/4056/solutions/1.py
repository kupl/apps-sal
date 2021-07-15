def leaderboard_sort(lbd, changes):
    lbd = lbd[:]
    for name,n in map(str.split, changes):
        n,i = int(n), lbd.index(name)
        lbd.pop(i)
        lbd.insert(i-n,name)
    return lbd

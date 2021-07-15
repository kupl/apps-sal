def points(games):
    res = 0
    for e in games:
        if e.split(':')[0] > e.split(':')[1]:
            res += 3
        elif e.split(':')[0] == e.split(':')[1]:
            res += 1
    return res

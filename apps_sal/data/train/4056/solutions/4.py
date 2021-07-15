def leaderboard_sort(leaderboard, changes):
    pos = leaderboard.copy()
    for name, change in map(str.split, changes):
        idx = pos.index(name)
        pos.insert(idx - int(change), pos.pop(idx))
    return pos

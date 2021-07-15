def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, offset = change.split(' ')
        pos = leaderboard.index(name)
        del leaderboard[pos]
        leaderboard.insert(pos - int(offset), name)
    return leaderboard


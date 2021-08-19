def leaderboard_sort(leaderboard, changes):
    for change in changes:
        (name, delta) = change.split()
        idx = leaderboard.index(name)
        leaderboard.insert(idx - int(delta), leaderboard.pop(idx))
    return leaderboard

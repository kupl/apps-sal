def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, step = change.split()
        step = int(step)
        idx = leaderboard.index(name)
        leaderboard.remove(name)
        leaderboard.insert(idx - step, name)
    return leaderboard

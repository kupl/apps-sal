def leaderboard_sort(leaderboard, changes):
    for c in changes:
        curr=leaderboard.index(c.split()[0])
        leaderboard.insert(curr-int(c.split()[1]),leaderboard.pop(curr))
    return leaderboard

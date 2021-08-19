def leaderboard_sort(leaderboard, changes):
    leaderboard.reverse()
    for (user, move) in [change.split() for change in changes]:
        index = leaderboard.index(user)
        leaderboard.remove(user)
        leaderboard.insert(eval('{}{}'.format(index, move)), user)
    leaderboard.reverse()
    return leaderboard

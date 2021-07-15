def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, move = change.split()
        value_index = leaderboard.index(name)

        leaderboard.remove(name)
        leaderboard.insert(value_index - int(move), name)

    return leaderboard

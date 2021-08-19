def leaderboard_sort(leaderboard, changes):
    change_dict = [(i.split()[0], int(i.split()[1])) for i in changes]
    leaderboard = leaderboard.copy()
    for (name, change) in change_dict:
        name_index = leaderboard.index(name)
        leaderboard.insert(name_index - change, leaderboard.pop(name_index))
    return leaderboard

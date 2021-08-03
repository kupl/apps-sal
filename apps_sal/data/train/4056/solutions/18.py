
def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, pos = change.split()
        old_pos = leaderboard.index(name)
        new_pos = eval(f"{old_pos}-{pos}")
        if old_pos < new_pos:
            leaderboard = leaderboard[:old_pos] + leaderboard[old_pos + 1:new_pos + 1] + [name] + leaderboard[new_pos + 1:]
        else:
            leaderboard = leaderboard[:new_pos] + [name] + leaderboard[new_pos:old_pos] + leaderboard[old_pos + 1:]
    return leaderboard

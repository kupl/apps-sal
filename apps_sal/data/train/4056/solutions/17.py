def leaderboard_sort(leaderboard, changes):
    for rec in changes:
        (name, move) = rec.split()
        curr_position = leaderboard.index(name)
        del leaderboard[curr_position]
        new_position = curr_position - int(move)
        leaderboard.insert(new_position, name)
    return leaderboard

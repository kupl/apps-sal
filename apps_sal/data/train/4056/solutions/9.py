def leaderboard_sort(leaderboard, changes):
    nleaderboard = leaderboard
    for change in changes:
        npos = int(change.split(" ")[1])
        name = change.split(" ")[0]
        pos = nleaderboard.index(name)
        if npos > 0:
            while npos != 0:
                nleaderboard[pos - 1], nleaderboard[pos] = nleaderboard[pos], nleaderboard[pos - 1]
                npos = npos - 1
                pos = pos - 1
        elif npos < 0:
            while npos != 0:
                leaderboard[pos + 1], leaderboard[pos] = leaderboard[pos], leaderboard[pos + 1]
                npos = npos + 1
                pos = pos + 1
    return nleaderboard

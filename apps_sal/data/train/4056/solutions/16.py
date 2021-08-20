def leaderboard_sort(leaderboard, changes):
    data = []
    for change in changes:
        data.append(change.split(' '))
        data[-1][1] = int(data[-1][1])
    for change in data:
        curr_i = leaderboard.index(change[0])
        shift_i = curr_i - change[1]
        if change[1] < 0:
            leaderboard.insert(shift_i + 1, leaderboard[curr_i])
        else:
            leaderboard.insert(shift_i, leaderboard[curr_i])
        if shift_i < curr_i:
            leaderboard.pop(curr_i + 1)
        else:
            leaderboard.pop(curr_i)
    return leaderboard

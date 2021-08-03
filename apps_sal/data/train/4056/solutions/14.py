def leaderboard_sort(leaderboard, changes):

    for i in range(len(changes)):

        loc = leaderboard.index(changes[i].split(" ")[0])

        leaderboard.insert(loc - int(changes[i].split(" ")[1]), leaderboard.pop(loc))

    return leaderboard

    # loop through changes implementing change
    # find person in board
    # pop them
    # insert back in new position

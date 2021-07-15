def leaderboard_sort(leaderboard, changes):
    leaderboard.reverse()
    length = len(leaderboard)
    for i in changes:
        temp = i.split(' ')
        k = temp[0]
        v = int(temp[1])
        for j in range(length):
            if leaderboard[j] == k:
                if j + v > length-1:
                    temp2 = leaderboard.pop(j)
                    leaderboard.insert(0, temp2)
                    break
                temp2 = leaderboard.pop(j)
                leaderboard.insert(j+v, temp2)
                break
    leaderboard.reverse()
    return leaderboard


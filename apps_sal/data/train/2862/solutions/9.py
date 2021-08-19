def leaderboard_climb(arr, kara):
    arr = sorted(set(arr), reverse=True)
    rank = []
    pos = len(arr)
    for x in kara:
        while pos >= 1 and x >= arr[pos - 1]:
            pos -= 1
        rank.append(pos + 1)
    return rank

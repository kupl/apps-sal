from bisect import bisect_left


def leaderboard_climb(arr, kara):
    result = []
    arr.append(float('inf'))
    arr = sorted([-a for a in set(arr)])
    for k in kara:
        i = bisect_left(arr, -k)
        result.append(i)
    return result

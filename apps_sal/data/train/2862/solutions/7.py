from bisect import bisect_left

def leaderboard_climb(arr, kara):
    arr.append(float('inf'))
    arr = sorted([-a for a in set(arr)])
    result = [bisect_left(arr, -k) for k in kara]
    return result

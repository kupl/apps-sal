from bisect import bisect


def leaderboard_climb(arr, kara):
    scoreboard = sorted(set(arr))
    scores = len(scoreboard)
    return [scores - bisect(scoreboard, i) + 1 for i in kara]

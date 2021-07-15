#Previously saved by accident before removing debug or refectoring.Doh!
import bisect
def leaderboard_climb(arr, kara):
    arr=sorted(list(set(arr)))
    return [(len(arr) + 1 -bisect.bisect_right(arr,score) ) for score in kara]

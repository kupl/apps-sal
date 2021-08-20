from collections import Counter


def points(dice):
    cnt = Counter(dice)
    val = set(cnt.values())
    if val == {5}:
        return 50
    if val == {1, 4}:
        return 40
    if val == {2, 3}:
        return 30
    return 20 * (val == {1, 1, 1, 1, 1} and all((cnt[a] for a in '345')))

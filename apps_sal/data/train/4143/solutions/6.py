from collections import Counter


def is_straight(dice):
    ds = sorted(map(int, dice))
    return ds == list(range(ds[0], ds[-1] + 1)) or ds == [1, 3, 4, 5, 6]


def points(dice):
    vs = Counter(dice).values()
    if 5 in vs:
        return 50
    elif 4 in vs:
        return 40
    elif 3 in vs and 2 in vs:
        return 30
    elif is_straight(dice):
        return 20
    else:
        return 0

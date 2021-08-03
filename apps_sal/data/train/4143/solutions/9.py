from collections import Counter


def points(dice):
    c = Counter(dice)
    if len(c) == 1:
        return 50

    elif len(c) == 2 and c.most_common()[0][1] == 4:
        return 40

    elif len(c) == 2 and c.most_common()[1][1] == 2:
        return 30

    else:
        s = sorted(int(x) for x in dice)
        if s[0] == s[1] or any(s[1:][i] + 1 != s[1:][i + 1] for i in range(len(s) - 2)):
            return 0

    return 20

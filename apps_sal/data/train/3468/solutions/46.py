from collections import Counter


def scramble(s1, s2):
    if set(s1) < set(s2):
        return False
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    cnt1.subtract(cnt2)
    notOk = [x < 0 for x in list(cnt1.values())]
    return not any(notOk)

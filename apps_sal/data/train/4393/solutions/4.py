from collections import Counter as Cnt


def repeat_sum(l):
    return sum((k for (k, v) in Cnt([e for ll in l for e in set(ll)]).items() if v > 1))

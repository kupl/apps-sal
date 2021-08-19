from collections import Counter


def scramble(s1, s2):
    one_split = list(s1)
    two_split = list(s2)
    count = 0
    copy = two_split[:]
    one = Counter(one_split)
    two = Counter(two_split)
    for x in two_split:
        if x not in list(two.keys()):
            return False
        if one[x] < two[x]:
            return False
    return True

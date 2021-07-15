from collections import Counter


def find_dup(lst):
    return Counter(lst).most_common()[0][0]

from collections import Counter


def sequence_classifier(arr):
    types = Counter([5, 1, 2, 3, 4, 0])
    for (a, b) in zip(arr, arr[1:]):
        if a == b:
            del types[1], types[3]
        if a != b:
            del types[5]
        if a < b:
            del types[3], types[4]
        if a > b:
            del types[1], types[2]
    return next(iter(types))

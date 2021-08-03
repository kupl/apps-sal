import collections


def number_of_pairs(gloves):
    return sum(i // 2 for i in collections.Counter(gloves).values())

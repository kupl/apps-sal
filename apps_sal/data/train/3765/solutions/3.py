from collections import defaultdict
from itertools import chain


def highest_age(group1, group2):
    total = defaultdict(int)
    for person in chain(group1, group2):
        total[person['name']] += person['age']
    return min(total, key=lambda p: (-total[p], p))

from collections import Counter
from itertools import chain


def highest_age(persons1, persons2):
    c = Counter()
    for p in chain(persons1, persons2):
        c[p['name']] += p['age']
    return min(iter(c.items()), key=lambda n_a: (-n_a[1], n_a[0]))[0] if c else None

from itertools import chain


def days_represented(trips):
    return len(set(chain(*(range(a, b + 1) for (a, b) in trips))))

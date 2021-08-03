from itertools import chain


def sum_of_intervals(intervals):
    return len(set(chain.from_iterable(range(*i) for i in intervals)))

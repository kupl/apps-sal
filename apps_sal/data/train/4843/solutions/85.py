from itertools import combinations
from operator import gt


def choose_best_sum(max_, count, distances):
    sums = list(filter(max_.__ge__, list(map(sum, combinations(distances, count)))))
    return max(sums) if sums else None

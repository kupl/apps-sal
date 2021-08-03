import itertools


def choose_best_sum(t, k, ls):
    return max([sum(row) for row in list(itertools.combinations(ls, k)) if sum(row) <= t], default=None)
# I have used itertools to find all combinations with 'k' towns possible from the list and found sum of all the combinations
# and stored that sum in a list if it is less than or equal to 't' and then found the max element of the list

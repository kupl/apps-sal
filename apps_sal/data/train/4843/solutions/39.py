import itertools


def choose_best_sum(t: int, k: int, ls: list) -> int:
    best_sum = 0
    best_set = None
    combinations = itertools.combinations(ls, k)
    for combination in combinations:
        combi_sum = sum(combination)
        if combi_sum <= t and combi_sum > best_sum:
            best_set = combination
            best_sum = combi_sum

    return None if best_sum == 0 else best_sum

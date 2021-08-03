import itertools


def choose_best_sum(max_sum, num_towns, distances):
    current_max = 0
    for sample in itertools.combinations(distances, num_towns):
        sum_sample = sum(sample)
        if sum_sample <= max_sum and sum_sample > current_max:
            current_max = sum_sample
    return current_max if current_max != 0 else None

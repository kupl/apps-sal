def count_positives_sum_negatives(x):
    return [] if len(x) == 0 else [sum([[x.count(i), 1][1] for i in x if i > 0]), sum([i for i in x if i < 0])]

def count_positives_sum_negatives(a):
    return a and [sum(i > 0 for i in a), sum(i for i in a if i < 0)]

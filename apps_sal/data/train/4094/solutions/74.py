def count_positives_sum_negatives(arr):
    if not arr:
        return []
    (n_pos, sum_neg) = (0, 0)
    for v in arr:
        if v > 0:
            n_pos += 1
        elif v < 0:
            sum_neg += v
    return [n_pos, sum_neg]

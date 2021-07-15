def count_positives_sum_negatives(arr):
    return arr and [sum(1 for a in arr if a > 0), sum(a for a in arr if a < 0)] or []

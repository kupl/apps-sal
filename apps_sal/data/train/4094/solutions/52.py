def count_positives_sum_negatives(arr):
    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)] if arr else []

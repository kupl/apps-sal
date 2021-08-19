def count_positives_sum_negatives(arr):
    return arr and [sum((1 for n in arr if n > 0)), sum((n for n in arr if n < 0))] or []

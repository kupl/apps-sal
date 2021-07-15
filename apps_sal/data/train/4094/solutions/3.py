def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []

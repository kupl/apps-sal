def count_positives_sum_negatives(arr):
    return [] if arr == [] else [sum((1 for x in arr if x > 0)), sum((x for x in arr if x < 0))]

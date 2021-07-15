def count_positives_sum_negatives(arr):
    return [[x>0 for x in arr].count(True), sum([x for x in arr if x < 0])] if arr else []

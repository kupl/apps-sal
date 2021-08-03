def count_positives_sum_negatives(arr):
    neg = [i for i in arr if i <= 0]
    return [len(arr) - len(neg), sum(neg)] if arr else []

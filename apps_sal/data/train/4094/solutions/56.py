def count_positives_sum_negatives(arr):
    neg = 0
    neg = sum((el for el in arr if el < 0))
    pos = 0
    pos = len([el for el in arr if el > 0])
    return [pos, neg] if arr else []

def count_positives_sum_negatives(arr):
    return [[sum(i>0 for i in arr), sum(i for i in arr if i < 0)],[]][arr==[]]

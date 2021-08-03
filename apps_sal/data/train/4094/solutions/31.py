def count_positives_sum_negatives(arr):
    result = [0, 0]
    for i in arr:
        result[i < 0] += 1 if (i > 0) else i
    return [] if (arr == []) else result

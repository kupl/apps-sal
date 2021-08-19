def count_positives_sum_negatives(arr):
    num = 0
    if len(arr) == 0:
        return []
    else:
        for x in arr:
            if x > 0:
                num += 1
        s = sum((x for x in arr if x < 0))
        return [num, s]

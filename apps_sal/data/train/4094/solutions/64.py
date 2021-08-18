def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    if arr:
        for x in arr:
            if x <= 0:
                negative += x
            else:
                positive += 1
        return [positive, negative]
    else:
        return []

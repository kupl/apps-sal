def count_positives_sum_negatives(arr):
    negativeTotal = 0
    positiveTotal = 0
    for i in arr:
        if i > 0:
            positiveTotal += 1
        else:
            negativeTotal += i
    if len(arr) == 0:
        return []
    else:
        return [positiveTotal, negativeTotal]

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    countPos = len([x for x in arr if x > 0])
    sumNeg = sum((x for x in arr if x < 0))
    return [countPos, sumNeg]

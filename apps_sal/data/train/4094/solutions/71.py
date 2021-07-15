def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    posTot = 0
    negSum = 0
    for number in arr:
        if number <= 0:
            negSum += number
        else:
            posTot += 1
    return [posTot,negSum]


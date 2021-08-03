def count_positives_sum_negatives(arr):
    res = [0, 0]
    for item in arr:
        if item > 0:
            res[0] += 1
        else:
            res[1] += item
    return res if arr else []

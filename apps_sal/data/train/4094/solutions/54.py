def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0
    if arr == []:
        return []
    for i in arr:
        if i > 0:
            pos = pos + 1
            print(pos)
        elif i < 0:
            neg = neg + i

    return [pos, neg]

def count_positives_sum_negatives(arr):
    neg_int = 0
    pos_int = 0
    if arr == []:
        return arr
    for i in arr:
        if i < 0:
            neg_int += i
        if i > 0:
            pos_int += 1
    return [pos_int, neg_int]

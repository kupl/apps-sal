def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    pos = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += 1
        else:
            neg += i
    a = [pos, neg]
    return a

def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0
    zer = 0
    for x in arr:
        if x < 0:
            neg += x
        elif x > 0:
            pos += 1
        else:
            zer += 0
    return [pos, neg] if zer != len(arr) else []

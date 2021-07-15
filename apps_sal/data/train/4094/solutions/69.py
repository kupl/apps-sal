def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0
    res = []
    if len(arr) > 0:
        for x in arr:
            if x > 0:
                pos += 1
            else:
                neg += x
        res.append(pos)
        res.append(neg)
    return res

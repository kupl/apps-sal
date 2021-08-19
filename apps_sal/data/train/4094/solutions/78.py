def count_positives_sum_negatives(arr):
    res = []
    pos = len([x for x in arr if x > 0])
    neg = sum([x for x in arr if x < 0])
    (res.append(pos), res.append(neg))
    return res if len(arr) > 0 else arr

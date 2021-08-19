def count_positives_sum_negatives(arr):
    p = 0
    n = 0
    if arr == []:
        return []
    for i in arr:
        if i != 0:
            if i > 0:
                p += 1
            else:
                n += i
    if p == 0 and n == 0:
        return [0, 0]
    return [p, n]

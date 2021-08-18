def count_positives_sum_negatives(arr):

    a = 0
    s = 0
    if not arr:
        return []

    for i in arr:
        if i > 0:
            a = a + 1
        else:
            s = s + i
    return [a, s]

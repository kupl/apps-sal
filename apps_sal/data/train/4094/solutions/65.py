def count_positives_sum_negatives(arr):
    a = []
    b = []
    if len(arr) == 0:
        return []
    for i in arr:
        if i > 0:
            a.append(i)
        elif i < 0:
            b.append(i)
    c = len(a)
    d = sum(b)
    m = [c, d]
    return m

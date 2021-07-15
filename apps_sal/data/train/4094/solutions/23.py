def count_positives_sum_negatives(arr):
    a = [0, 0]
    for i in arr:
        if i < 0:
            a[1] += i
        elif i > 0:
            a[0] += 1
    return a if arr else []

def count_positives_sum_negatives(arr):
    (count, sumnegative) = (0, 0)
    for e in arr:
        if e > 0:
            count += 1
        else:
            sumnegative += e
    return [] if arr == [] else [count, sumnegative]

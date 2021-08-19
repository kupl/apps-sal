def count_positives_sum_negatives(arr):
    i = j = 0
    if not arr:
        return []
    for num in arr:
        if num > 0:
            i += 1
        elif num < 0:
            j += num
        else:
            pass
    return [i, j]

def count_positives_sum_negatives(arr):
    if arr:
        a = 0
        b = 0
        for i in arr:
            if i > 0:
                a += 1
            elif i <= 0:
                b += i
        return [a, b]
    else:
        return []

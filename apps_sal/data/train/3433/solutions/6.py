def replace_zero(arr):
    (max_idx, count) = (None, 0)
    left = idx = right = 0
    for (i, n) in enumerate(arr + [0]):
        if n:
            right += 1
        else:
            if left + right >= count:
                (max_idx, count) = (idx, left + right)
            (left, idx, right) = (right, i, 0)
    return max_idx

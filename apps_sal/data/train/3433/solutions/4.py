def replace_zero(arr):
    (best_len, best_idx) = (0, 0)
    (curr_len, curr_idx) = (0, None)
    for (i, e) in enumerate(arr):
        if e == 1:
            curr_len += 1
        else:
            if curr_len >= best_len:
                (best_len, best_idx) = (curr_len, curr_idx)
            if curr_idx is None:
                curr_len += 1
            elif i - curr_idx < 2:
                curr_len = 1
            else:
                curr_len = i - curr_idx
            curr_idx = i
    if curr_len >= best_len:
        (best_len, best_idx) = (curr_len, curr_idx)
    return best_idx

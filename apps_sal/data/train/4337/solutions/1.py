def swap_head_tail(lst):
    (n, d) = divmod(len(lst), 2)
    return lst[n + d:] + [lst[n]] * d + lst[:n]

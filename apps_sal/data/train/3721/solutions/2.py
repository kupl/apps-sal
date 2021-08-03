def catch_sign_change(lst):
    return sum((a or 1) * (b or 1) < 0 for a, b in zip(lst, lst[1:]))

def catch_sign_change(lst):
    return sum((x >= 0) != (y >= 0) for x, y in zip(lst, lst[1:]))

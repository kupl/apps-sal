def catch_sign_change(lst):
    return sum(((a < 0) != (b < 0) for (a, b) in zip(lst, lst[1:])))

def catch_sign_change(lst):
    return sum((m < 0) == (n > -1) for m, n in zip(lst, lst[1:]))

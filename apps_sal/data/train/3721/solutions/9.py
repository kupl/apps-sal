def catch_sign_change(lst):
    return sum((1 for (a, b) in zip(lst, lst[1:]) if (a < 0) != (b < 0)))

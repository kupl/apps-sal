def unique_sum(lst):
    def y(x): return sum(set(x))
    if len(lst) == 0:
        return None
    elif y(lst) == 0:
        return 0
    else:
        return y(lst)

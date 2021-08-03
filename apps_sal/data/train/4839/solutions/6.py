from math import ceil


def new_avg(lst, newavg):
    nxt = newavg * (len(lst) + 1) - sum(lst)
    if nxt <= 0:
        raise ValueError
    return ceil(nxt)

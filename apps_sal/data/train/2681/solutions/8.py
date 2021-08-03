from math import ceil, log


def bouncing_ball(initial, proportion):
    return ceil(-log(initial - 1e-9, proportion))

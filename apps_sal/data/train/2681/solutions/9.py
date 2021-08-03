from math import ceil, log


def bouncing_ball(initial, proportion):
    return ceil(log(1 / initial, proportion))

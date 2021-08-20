from functools import reduce


def crashing_weights(weights):
    return reduce(crash_if_heavier, weights)


def crash_if_heavier(upper_row, lower_row):
    return [wl if wu <= wl else wu + wl for (wu, wl) in zip(upper_row, lower_row)]

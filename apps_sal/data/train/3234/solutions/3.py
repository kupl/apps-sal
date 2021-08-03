import numpy as np


def calc_one(value, tot_sum, tot_prod):
    value[value == tot_sum] = np.nan
    return (tot_prod / value) / (tot_sum - value)


def select_subarray(arr):
    np_arr = np.array(arr).astype(np.float64)
    tot_sum = np_arr.sum()
    tot_prod = np_arr.prod()
    qs = np.apply_along_axis(
        calc_one,
        0,
        np_arr,
        tot_sum,
        tot_prod,
    )
    qs = np.abs(qs)
    min_ = np.nanmin(qs)
    where_min = np.where(qs == min_)[0]
    out = [[where, arr[where]] for where in where_min]
    return out if len(out) > 1 else out[0]

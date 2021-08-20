from math import ceil


def new_avg(arr, newavg):
    required = ceil(newavg * (len(arr) + 1) - sum(arr))
    assert required > 0
    return required

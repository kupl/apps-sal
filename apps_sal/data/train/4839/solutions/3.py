from math import ceil

def new_avg(arr, newavg):
    # calculate the required amount
    required = ceil(newavg * (len(arr) + 1) - sum(arr))
    # throw an error if non-positive
    assert required > 0
    # otherwise return result
    return required

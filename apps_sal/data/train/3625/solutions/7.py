import numpy as np
from itertools import groupby


def sum_of_regular_numbers(arr):
    lst = [list(g) for (k, g) in groupby(np.diff(arr))]
    (idx, ans) = (0, 0)
    for i in lst:
        if len(i) > 1:
            ans += sum(arr[idx:idx + len(i) + 1])
        idx = idx + len(i)
    return ans

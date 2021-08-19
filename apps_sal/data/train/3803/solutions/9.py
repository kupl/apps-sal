from functools import reduce
from collections import Counter


def update_inventory(cur_stock, new_stock):
    return sorted([(v, k) for (k, v) in reduce(lambda x, y: x + y, [Counter({k: v for (v, k) in x}) for x in [cur_stock, new_stock]]).items()], key=lambda x: x[1])

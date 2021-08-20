from collections import Counter


def update_inventory(cur_stock, new_stock):
    c = Counter({key: value for (value, key) in cur_stock}) + Counter({key: value for (value, key) in new_stock})
    return [(c[key], key) for key in sorted(c)]

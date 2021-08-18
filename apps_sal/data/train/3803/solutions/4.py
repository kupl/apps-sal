from collections import Counter


def update_inventory(cur_stock, new_stock):
    C1 = Counter({v: k for k, v in cur_stock})
    C2 = Counter({v: k for k, v in new_stock})
    return [(v, k) for k, v in sorted((C1 + C2).items())]

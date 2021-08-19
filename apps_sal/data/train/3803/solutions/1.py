from collections import defaultdict


def update_inventory(cur_stock, new_stock):
    stock = defaultdict(int, [(k, v) for (v, k) in cur_stock])
    for (v, k) in new_stock:
        stock[k] += v
    return [(v, k) for (k, v) in sorted(stock.items())]

from collections import defaultdict


def update_inventory(prv_stock, add_stock):
    new_stock = defaultdict(int, (item[::-1] for item in prv_stock))
    for (qty, prod) in add_stock:
        new_stock[prod] += qty
    return [item[::-1] for item in sorted(new_stock.items())]

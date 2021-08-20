def update_inventory(cur_stock, new_stock):
    d = {}
    for (i, j) in cur_stock + new_stock:
        d[j] = d.get(j, 0) + i
    return sorted([(j, i) for (i, j) in d.items()], key=lambda x: x[1])

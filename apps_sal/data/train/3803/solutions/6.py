def update_inventory(cur_stock, new_stock):
    cur_stock_dict = {key: value for (value, key) in cur_stock}
    for (value, key) in new_stock:
        cur_stock_dict[key] = cur_stock_dict.get(key, 0) + value
    return [(cur_stock_dict[key], key) for key in sorted(cur_stock_dict)]

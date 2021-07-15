def inverse_slice(items, a, b):
    inv_list=items[0:a]
    inv_list.extend(items[b:])
    return inv_list

def delete_nth(order, max_e):
    return [o for (i, o) in enumerate(order) if order[:i].count(o) < max_e]

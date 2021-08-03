def delete_nth(order, max_e):
    return [order[i] for i in range(len(order)) if order[0:i + 1].count(order[i]) <= max_e]

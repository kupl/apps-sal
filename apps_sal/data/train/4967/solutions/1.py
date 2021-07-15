def knapsack(c, items):
    qtys = [0 for i in items]
    weights = sorted(items, reverse=True, key=lambda (size, value): float(value)/size)
    for (size, value) in weights:
        qty = c // size
        qtys[items.index((size, value))] = qty
        c -= qty * size
    return qtys

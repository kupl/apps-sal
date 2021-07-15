def knapsack(capacity, items):
    quantities = [0] * len(items)
    for idx, (size, value) in sorted(enumerate(items),
                key=lambda it: it[1][1] / it[1][0], reverse=True):
        quantities[idx], capacity = divmod(capacity, size)
    return quantities

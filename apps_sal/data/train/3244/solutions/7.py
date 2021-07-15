def cheapest_quote(n):
    price, costs = 0, [(1, 0.1), (5, 0.49), (10, 0.97), (20, 1.93), (40, 3.85)]
    while n:
        quantity, cost = costs.pop()
        price += (n // quantity) * cost
        n %= quantity
    return round(price, 2)

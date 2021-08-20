costs = [(3.85, 40), (1.93, 20), (0.97, 10), (0.49, 5), (0.1, 1)]


def cheapest_quote(n):
    price = 0
    for (cost, qty) in costs:
        (q, n) = divmod(n, qty)
        price += cost * q
    return round(price, 2)

def cheapest_quote(n):
    rates = [(40, 3.85), (20, 1.93), (10, 0.97), (5, 0.49), (1, 0.1)]
    total = 0
    for bundle, price in rates:
        total += n // bundle * price
        n %= bundle
    return round(total, 2)

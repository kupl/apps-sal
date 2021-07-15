def cheapest_quote(n):
    prices = [(40, 3.85), (20, 1.93), (10, 0.97), (5, 0.49), (1, 0.10)]
    result = 0
    for q, c in prices:
        result += n // q * c
        n = n % q
    return round(result, 2)
        


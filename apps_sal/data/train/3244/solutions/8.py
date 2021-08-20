bundles = {40: 3.85, 20: 1.93, 10: 0.97, 5: 0.49, 1: 0.1}


def cheapest_quote(n):
    if n == 0:
        return 0.0
    for i in [40, 20, 10, 5, 1]:
        if n - i > -1:
            return round(int(n / i) * bundles[i] + cheapest_quote(n % i), 2)

def four_piles(n, y):
    x = round(n / (2 + y + 1 / y))
    ls = [x + y, x - y, x * y, x / y]
    return ls if x - y > 0 and x % y == 0 and sum(ls) == n else []

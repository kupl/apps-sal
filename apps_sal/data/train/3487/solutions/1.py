from itertools import count


def beeramid(bonus, price):
    bonus = max(bonus, 0)
    n = bonus // price
    return next(x for x in count(int((n * 3)**(1 / 3) + 1), -1) if x * (x + 1) * (2 * x + 1) // 6 <= n)

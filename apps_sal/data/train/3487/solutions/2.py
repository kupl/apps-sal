def beeramid(bonus, price):
    k = bonus // price
    d = (3 * (11664 * k * k - 3) ** 0.5 + 324 * k) ** (1 / 3)
    n = (d / 3 + 1 / d - 1) / 2
    return k > 0 and int(n.real + 1e-12)

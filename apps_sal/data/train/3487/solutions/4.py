def beeramid(bonus, price, level=1):
    return 0 if bonus < price * level**2 else 1 + beeramid(bonus - price * level**2, price, level + 1)


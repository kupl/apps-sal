def beeramid(bonus, price):
    num_cans = bonus // price
    level = 0
    while num_cans >= 0:
        level += 1
        num_cans -= level*level
    return max(0, level-1)

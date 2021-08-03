from math import ceil


def order(pizzas, salads, appetizers):
    p = (pizzas / 2) * 3 + ceil(pizzas / 10) * 10
    sa = 3 * salads + 5 * appetizers
    return max(p, sa)

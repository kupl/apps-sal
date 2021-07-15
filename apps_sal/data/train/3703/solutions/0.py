from math import ceil

def order(pizzas, salads, appetizers):
    tp = 3 * pizzas / 2 + 10 * math.ceil(pizzas / 10)
    ts = 3 * salads + 5 * appetizers
    return max(tp, ts)


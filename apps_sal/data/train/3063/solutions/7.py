from collections import defaultdict
from statistics import mean
prices = defaultdict(lambda: 9)
prices.update(dict.fromkeys(['banana', 'orange', 'apple', 'lemon', 'grapes'], 5))
prices.update(dict.fromkeys(['avocado', 'strawberry', 'mango'], 7))


def mix_fruit(arr):
    return round(mean((prices[fruit.lower()] for fruit in arr)))

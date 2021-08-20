PRICES = dict(banana=5, orange=5, apple=5, lemon=5, grapes=5, avocado=7, strawberry=7, mango=7)


def mix_fruit(fruits):
    return round(sum((PRICES.get(fruit.lower(), 9) for fruit in fruits)) / len(fruits))

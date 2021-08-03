import random


def actually_really_good(foods):
    if not foods:
        return "You know what's actually really good? Nothing!"
    food1, food2 = random.sample(foods, 2) if len(foods) > 1 else foods + ["more {}".format(foods[0])]
    return "You know what's actually really good? {} and {}.".format(food1.capitalize(), food2.lower())

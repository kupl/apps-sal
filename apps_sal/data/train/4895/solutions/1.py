import random
def actually_really_good(foods):
    if foods == []: return "You know what's actually really good? Nothing!"
    elif len(foods) == 1:
        s = random.choice(foods)
        return "You know what's actually really good? " + s.capitalize() + " and more " + s.lower() + "."
    else:
        return "You know what's actually really good? " + random.choice(foods).capitalize() + " and more " + random.choice(foods).lower() + "."


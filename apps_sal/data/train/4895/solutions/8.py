from random import shuffle


def actually_really_good(foods):
    if not foods:
        return "You know what's actually really good? Nothing!"
    elif len(foods) == 1:
        return "You know what's actually really good? {0} and more {1}.".format(foods[0].capitalize(), foods[0].lower())
    elif len(foods) > 2:
        shuffle(foods)
    return "You know what's actually really good? {0} and {1}.".format(foods[0].capitalize(), foods[1].lower())

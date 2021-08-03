from random import choice


def actually_really_good(foods):
    res, foods = 'Nothing!', [f.lower() for f in foods]
    if len(foods) == 1:
        res = "{} and more {}.".format(foods[0].capitalize(), foods[0])
    elif len(foods) >= 2:
        res = "{} and {}.".format(foods[0].capitalize(), choice(foods[1:]))
    return "You know what's actually really good? {}".format(res)

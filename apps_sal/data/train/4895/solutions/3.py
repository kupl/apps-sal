def actually_really_good(foods):
    if len(foods) > 1:
        good = '{} and {}.'.format(foods[0].capitalize(), foods[1].lower())
    elif len(foods) == 1:
        good = '{} and more {}.'.format(foods[0].capitalize(), foods[0].lower())
    else:
        good = 'Nothing!'
    return "You know what's actually really good? {}".format(good)

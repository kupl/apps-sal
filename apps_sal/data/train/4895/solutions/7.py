def actually_really_good(foods):
    return "You know what's actually really good? {}".format('Nothing!' if not foods else '{} and {}.'.format(str.capitalize(foods[0]), (foods[1] if len(foods) > 1 else 'more %s' % foods[0]).lower()))

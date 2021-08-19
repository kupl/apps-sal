def actually_really_good(a):
    return "You know what's actually really good? " + (a and '%s and %s.' % (a[0], 'more ' * (a[0] == a[-1]) + a[-1]) or 'Nothing!').capitalize()

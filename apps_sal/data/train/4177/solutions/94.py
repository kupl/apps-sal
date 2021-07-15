def men_from_boys(a):
    men = sorted([x for x in set(a) if x % 2 == 0])
    boys = sorted([x for x in set(a) if x % 2 != 0])[::-1]
    return men + boys

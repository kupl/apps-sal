from functools import reduce


def choose(a, b):
    if a[1] < b[1]:
        return b
    if a[1] > b[1]:
        return a
    return a if a[0] < b[0] else b


def highest_age(group1, group2):
    totals = {}
    for item in group1 + group2:
        name = item['name']
        totals[name] = totals.get(name, 0) + item['age']
    return reduce(lambda acc, x: choose(acc, x), totals.items(), ('', -1))[0]

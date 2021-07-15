from itertools import groupby
def london_city_hacker(journey):
    tube_fare = lambda n: 2.4 * n
    bus_fare = lambda n: 1.5 * sum(divmod(n, 2))
    s = sum([bus_fare, tube_fare][a](len(list(g))) for a, g in groupby(map(lambda a: isinstance(a, str), journey)))
    return f'£{s:.2f}'

def calc_fuel(n):
    from math import floor
    fuels = {'lava': 800, 'blaze rod': 120, 'coal': 80, 'wood': 15, 'stick': 1}
    n *= 11
    result = {}
    for (fuel, time) in fuels.items():
        (result[fuel], n) = divmod(n, time)
    return result

from itertools import cycle


def blocks_to_collect(level):
    materials = cycle(('gold', 'diamond', 'emerald', 'iron'))
    res = {'total': 0, 'gold': 0, 'diamond': 0, 'emerald': 0, 'iron': 0}
    for x in range(3, 2 * level + 2, 2):
        material = next(materials)
        res[material] += x ** 2
        res['total'] += x ** 2
    return res

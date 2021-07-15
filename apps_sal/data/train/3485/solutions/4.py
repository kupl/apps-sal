density_order = {key: i for i, key in enumerate(['O','A','W','H'])}

def separate_liquids(glass):
    lst_of_liquids = iter(sorted([liquid for row in glass for liquid in row], key=lambda d: density_order[d]))
    return [[next(lst_of_liquids) for j in range(0, len(glass[0]))] for i in range(0, len(glass))]

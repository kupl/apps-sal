density = {'H':4, 'W':3, 'A':2, 'O':1}


def separate_liquids(glass):
    glass_ = sorted([x for i in glass for x in i], key=lambda elem: density.get(elem))
    for row in glass:
        for i in range(len(row)):
            row[i] = glass_.pop(0)
    return glass


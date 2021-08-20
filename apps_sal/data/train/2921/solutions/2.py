def blocks_to_collect(height):
    stuff = [0, 0, 0, 0]
    for level in range(height):
        stuff[level % 4] += (2 * level + 3) ** 2
    return dict(list(zip(('gold', 'diamond', 'emerald', 'iron', 'total'), stuff + [sum(stuff)])))

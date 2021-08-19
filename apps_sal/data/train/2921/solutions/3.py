def blocks_to_collect(level):
    beacon = {x: 0 for x in 'total gold diamond emerald iron'.split(' ')}
    for l in range(1, level + 1):
        mode = 'gold diamond emerald iron'.split(' ')[(l - 1) % 4]
        blocks = (2 * l + 1) ** 2
        beacon['total'] += blocks
        beacon[mode] += blocks
    return beacon

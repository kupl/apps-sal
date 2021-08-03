classes = {
    'warrior': (4, [11, 8, 12, 13, 13, 11, 9, 9]),
    'knight': (5, [14, 10, 10, 11, 11, 10, 9, 11]),
    'wanderer': (3, [10, 11, 10, 10, 14, 12, 11, 8]),
    'thief': (5, [9, 11, 9, 9, 15, 10, 12, 11]),
    'bandit': (4, [12, 8, 14, 14, 9, 11, 8, 10]),
    'hunter': (4, [11, 9, 11, 12, 14, 11, 9, 9]),
    'sorcerer': (3, [8, 15, 8, 9, 11, 8, 15, 8]),
    'pyromancer': (1, [10, 12, 11, 12, 9, 12, 10, 8]),
    'cleric': (2, [11, 11, 9, 12, 8, 11, 8, 14]),
    'deprived': (6, [11, 11, 11, 11, 11, 11, 11, 11])
}
levelup_souls = [0, 0, 673, 690, 707, 724, 741, 758, 775, 793, 811, 829]


def souls(character, build):
    level, stats = classes[character]
    up_level = sum(build) - sum(stats) + level
    s = 0
    for l in range(level + 1, up_level + 1):
        if l < 12:
            s += levelup_souls[l]
        else:
            s += round(pow(l, 3) * 0.02 + pow(l, 2) * 3.06 + 105.6 * l - 895)
    return 'Starting as a {}, level {} will require {} souls.'.format(character, up_level, s)

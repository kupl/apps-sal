BASE = {'warrior': (4, 86), 'knight': (5, 86), 'wanderer': (3, 86), 'thief': (5, 86), 'bandit': (4, 86), 'hunter': (4, 86), 'sorcerer': (3, 82), 'pyromancer': (1, 84), 'cleric': (2, 84), 'deprived': (6, 88)}


def souls(s, a):
    (n, b) = BASE[s]
    m = sum(a) - b
    r = sum([673, 690, 707, 724, 741, 758, 775, 793, 811, 829][n - 1:n + m - 1]) + sum((round(i ** 3 * 0.02 + i ** 2 * 3.06 + 105.6 * i - 895) for i in range(12, n + m + 1)))
    return f'Starting as a {s}, level {n + m} will require {r} souls.'

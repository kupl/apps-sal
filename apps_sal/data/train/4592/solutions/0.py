from itertools import product


def winning_lines(size, dimension):
    if dimension == 1:
        return frozenset({frozenset({(n,) for n in range(size)})})
    lines = set()
    for (line, idx, val) in product(winning_lines(size, dimension - 1), range(dimension), range(size)):
        lines.add(frozenset({cell[:idx] + (val,) + cell[idx:] for cell in line}))
    for dirs in product((-1, 1), repeat=dimension - 1):
        lines.add(frozenset(zip(*(range(size)[::d] for d in [1] + list(dirs)))))
    return lines


def play_OX_3D(moves):
    (grid, lines) = ([], winning_lines(4, 3))
    for m in moves:
        grid.append(tuple(m))
        if any((line <= set(grid[-1::-2]) for line in lines)):
            return '{} wins after {} moves'.format('XO'[len(grid) % 2], len(grid))
    return 'No winner'

from itertools import chain, product


def unique_products(sets, excluding=frozenset()):
    """
    Calculates cartesian product between the sets passed as parameter, only keeping products with unique numbers.
    """
    if not sets:
        yield ()
        return
    for x in sets[0] - excluding:
        for rest in unique_products(sets[1:], excluding | {x}):
            yield (x,) + rest

def solve_column(column, clue):
    # First calculates all valid fillings with the given column, than merges the solutions in a single list where each
    # cell is the set containing the values in the same position of each solution.
    # [column=[{1, 2, 3}, {1, 2, 3}, {1, 2}, {4}], clue=2] -> [(3, 1, 2, 4), (3, 2, 1, 4)] -> [{3}, {1, 2}, {1, 2}, {4}]
    combos = [set(x) for x in list(zip(*[x for x in unique_products(column) if see(x) == clue]))]
    for i in range(len(column)):
        column[i] -= column[i] - combos[i]


def see(column):
    """
    Calculates how many buildings can be viewed.
    """
    visible = tallest = 0
    for building in column:
        visible += building > tallest
        tallest = max(building, tallest)
    return visible

def simplify(column, clue, n):
    if clue is 1:
        column[0] -= set(range(1, n))  # the highest building must be in the first cell
    elif clue > 0:  # if clue is 0 means no hint
        for i in range(clue - 1):
            column[i] -= set(range(n, n + i + 1 - clue, -1))
        solve_column(column, clue)


def solve_cross(city, x, y):
    """
    Removes from the same row and column the number found at (x, y), if the cell contains only one number.
    :type city: list of (list of set)
    """
    if len(city[x][y]) is not 1:
        solve_uniqueness(city, x, y)
        return
    for i in chain(range(x), range(x + 1, len(city))):
        city[i][y] -= city[x][y]
    for j in chain(range(y), range(y + 1, len(city))):
        city[x][j] -= city[x][y]


def solve_uniqueness(city, x, y):
    """
    Checks if one of the numbers in the cell city[x][y] compares only once in the same row / column.
    """
    for n in city[x][y]:  # checks if a number appears only once in the row / column
        if not any([n in city[i][y] for i in chain(range(x), range(x + 1, len(city)))]) or \
                not any([n in city[x][j] for j in chain(range(y), range(y + 1, len(city)))]):
            city[x][y].clear()
            city[x][y].add(n)
            solve_cross(city, x, y)
            break


def solve(n, clues):
    city = list(list(set(range(1, n + 1)) for i in range(n)) for j in range(n))
    while not all([len(cell) is 1 for row in city for cell in row]):
        for i in range(n):
            for j in range(n):
                simplify([city[k][j] for k in range(n)], clues[i * n + j], n)
            for s in range(n):
                for t in range(n):
                    solve_cross(city, s, t)
            city = [list(row) for row in reversed(list(zip(*city)))]  # rotates the city 90° anti-clockwise
    return tuple(tuple(cell.pop() for cell in row) for row in city)
    
solve_puzzle = lambda x: solve(4, x)

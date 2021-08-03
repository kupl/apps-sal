from copy import deepcopy

pieces = {}
solution = []


def fits_at(grid, p, y, x):
    nonlocal pieces
    for pos in pieces[p]:
        py = y + pos[0]
        if py < 0 or py >= len(grid):
            return False
        px = x + pos[1]
        if px < 0 or px >= len(grid[0]):
            return False
        if grid[py][px] != 0:
            return False
    return True


def rec_solve(grid, items):
    nonlocal pieces, solution
    if items == [] or solution != []:
        return

    # fit 1st piece
    val = items[0]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if fits_at(grid, val, y, x):
                # piece fits
                # place piece
                for pos in pieces[val]:
                    grid[y + pos[0]][x + pos[1]] = val
                # recursive solve
                next_list = items[1:]
                rec_solve(grid, next_list)
                if next_list == []:
                    solution = deepcopy(grid)
                    return
                # remove piece
                for pos in pieces[val]:
                    grid[y + pos[0]][x + pos[1]] = 0


def fit_bag(height: int, width: int, items: List[List[List[int]]]) -> List[List[int]]:
    # make list of relative positions from an empty grid position
    nonlocal pieces, solution
    solution = []
    item_ids = []
    for item in items:
        i = 0
        while item[0][i] == 0:
            i += 1
        anchor = [0, i]
        val = item[0][i]

        # generate list of coordinates relative to anchor
        rel_c = []
        for h in range(len(item)):
            for w in range(len(item[0])):
                if item[h][w] != 0:
                    newpos = [h, w - i]
                    rel_c.append(newpos)
        pieces[val] = rel_c
        item_ids.append(val)

    grid = [[0 for x in range(width)] for y in range(height)]
    rec_solve(grid, item_ids)
    return solution

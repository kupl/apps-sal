from copy import deepcopy


class Nonogram:
    POS = {(2, 2): ((1, 1, 0, 1, 1),), (5,): ((1, 1, 1, 1, 1),), (1, 1, 1): ((1, 0, 1, 0, 1),), (1, 3): ((1, 0, 1, 1, 1),), (3, 1): ((1, 1, 1, 0, 1),), (4,): ((1, 1, 1, 1, 0), (0, 1, 1, 1, 1)), (1, 2): ((1, 0, 0, 1, 1), (1, 0, 1, 1, 0), (0, 1, 0, 1, 1)), (2, 1): ((1, 1, 0, 0, 1), (1, 1, 0, 1, 0), (0, 1, 1, 0, 1)), (3,): ((1, 1, 1, 0, 0), (0, 1, 1, 1, 0), (0, 0, 1, 1, 1)), (2,): ((1, 1, 0, 0, 0), (0, 1, 1, 0, 0), (0, 0, 1, 1, 0), (0, 0, 0, 1, 1)), (1,): ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 1)), (1, 1): ((1, 0, 1, 0, 0), (1, 0, 0, 1, 0), (1, 0, 0, 0, 1), (0, 1, 0, 1, 0), (0, 1, 0, 0, 1), (0, 0, 1, 0, 1))}

    def __init__(self, clues):
        self.clues = {'V': clues[0], 'H': clues[1]}

    def solve(self):
        grid = {(d, z): list(self.POS[self.clues[d][z]]) for d in 'VH' for z in range(5)}
        changed = True
        while changed:
            changed = False
            for x in range(5):
                for y in range(5):
                    (tupH, iH, tupV, iV) = (('H', x), y, ('V', y), x)
                    if len(grid[tupH]) == 1 and len(grid[tupV]) == 1:
                        continue
                    vH = {v[iH] for v in grid[tupH]}
                    vV = {v[iV] for v in grid[tupV]}
                    target = vH & vV
                    if len(vH) == 2 and len(target) == 1:
                        changed = True
                        grid[tupH] = [t for t in grid[tupH] if t[iH] in target]
                    if len(vV) == 2 and len(target) == 1:
                        changed = True
                        grid[tupV] = [t for t in grid[tupV] if t[iV] in target]
        return tuple((grid['H', n][0] for n in range(5)))

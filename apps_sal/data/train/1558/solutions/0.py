"""
Code chef problem DESTCELL, Destroy Cells
"""


def find_destroyed_cells(cell_advance, n, m, k):
    row = 1
    col = 1
    destroyed_cells = {(1, 1)}
    while True:
        row, col = cell_advance(row, col, n, m, k)
        if row <= n and col <= m:
            destroyed_cells.add((row, col))
        else:
            break
    return destroyed_cells


def cell_advance_hero1(row, col, n, m, k):
    return row + (col + k) // m, (col + k) % m + 1


def cell_advance_hero2(row, col, n, m, k):
    return (row + k) % n + 1, col + (row + k) // n


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(s) for s in input().split(' ')]
        counts = []
        for k in range(n * m):
            cells_h1 = find_destroyed_cells(cell_advance_hero1, n, m, k)
            cells_h2 = find_destroyed_cells(cell_advance_hero2, n, m, k)

            destroyed = len(cells_h1) + len(cells_h2) - len(cells_h1 & cells_h2)
            counts.append(destroyed)
        print(' '.join([str(c) for c in counts]))


main()

from enum import IntEnum
from typing import List, Tuple, Set


class Tile(IntEnum):
    LAND = 0
    WATER = 1


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        assert height > 0, f\"Grid must have at least one row but has {height} rows\"
        width = len(grid[0])
        seen_land: List[List[bool]] = [
            [False for _ in range(width)] for _ in range(height)
        ]

        num_islands = 0
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                if tile != Tile.LAND or seen_land[y][x]:
                    continue
                else:
                    to_check = {(x, y)}
                    is_island = True
                    while to_check:
                        x1, y1 = to_check.pop()
                        seen_land[y1][x1] = True
                        is_island &= 0 < x1 < width - 1 and 0 < y1 < height - 1
                        for (x2, y2) in [
                            (x1 - 1, y1),
                            (x1 + 1, y1),
                            (x1, y1 - 1),
                            (x1, y1 + 1),
                        ]:
                            if (
                                0 <= x2 < width
                                and 0 <= y2 < height
                                and not seen_land[y2][x2]
                                and grid[y2][x2] == Tile.LAND
                            ):
                                to_check.add((x2, y2))
                    if is_island:
                        num_islands += 1
        return num_islands

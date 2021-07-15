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

        def delete_connected_land(x: int, y: int) -> None:
            if grid[y][x] == Tile.WATER:
                return
            grid[y][x] = Tile.WATER
            if x > 0:
                delete_connected_land(x - 1, y)
            if y > 0:
                delete_connected_land(x, y - 1)
            if x < width - 1:
                delete_connected_land(x + 1, y)
            if y < height - 1:
                delete_connected_land(x, y + 1)

        for y in [0, height - 1]:
            for x in range(width):
                delete_connected_land(x, y)

        for y in range(height):
            for x in [0, width - 1]:
                delete_connected_land(x, y)

        num_islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if grid[y][x] == Tile.LAND:
                    num_islands += 1
                    delete_connected_land(x, y)
        return num_islands

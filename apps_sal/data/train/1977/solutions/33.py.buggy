from typing import List, Tuple, Set


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        assert height > 0, f\"Grid must have at least one row but has {len(grid)} rows\"
        width = len(grid[0])
        seen_land: Set[Tuple[int, int]] = set()

        def mark_all_connected_and_check_is_island(point_x: int, point_y: int) -> int:
            seen_land.add((point_x, point_y))
            is_island = (
                point_x != 0
                and point_y != 0
                and point_x < width - 1
                and point_y < height - 1
            )
            for (x, y) in [
                (point_x - 1, point_y),
                (point_x + 1, point_y),
                (point_x, point_y - 1),
                (point_x, point_y + 1),
            ]:
                try:
                    if grid[y][x] != 0:
                        continue
                except IndexError:
                    continue
                if (x, y) in seen_land:
                    continue
                is_island &= mark_all_connected_and_check_is_island(x, y)
            return is_island

        num_islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 1:
                    continue
                elif cell == 0:
                    if (x, y) not in seen_land:
                        is_island = mark_all_connected_and_check_is_island(x, y)
                        if is_island:
                            num_islands += 1
                else:
                    assert False, f\"Cell ({x},{y}) is {cell} but expected 0 or 1\"
        return num_islands


def test_example_1() -> None:
    assert (
        Solution().closedIsland(
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ]
        )
        == 2
    )


def test_example_2() -> None:
    assert (
        Solution().closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]])
        == 1
    )


def test_example_3() -> None:
    assert (
        Solution().closedIsland(
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
            ]
        )
        == 2
    )


def test_simplest_grids() -> None:
    assert Solution().closedIsland([[0]]) == 0
    assert Solution().closedIsland([[1]]) == 0


def test_simplest_island() -> None:
    assert Solution().closedIsland([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 1


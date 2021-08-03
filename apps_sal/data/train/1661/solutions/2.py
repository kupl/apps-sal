import re
from enum import Enum
from operator import itemgetter
from typing import List, Tuple, Set, Generator, Match


Cell = Tuple[int, int]


class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)


def execute(code: str) -> str:
    visited_cells = visit_cells(code)
    path = draw_path(visited_cells)
    return path


def visit_cells(code: str) -> Set[Cell]:
    visited_cells = [(0, 0)]
    direction = Direction.RIGHT

    for action, n_times in code_interpreter(code):
        if action == 'F':
            new_cells = move_forward(visited_cells[-1], direction, n_times)
            visited_cells.extend(new_cells)
        else:
            direction = make_turn(direction, action, n_times)
    return set(visited_cells)


def code_interpreter(code: str) -> Generator[Tuple[str, int], None, None]:
    code = unroll_code(code)
    for move in re.finditer(r'([LRF])(\d*)', code):
        action = move.group(1)
        n_times = int(move.group(2)) if move.group(2) else 1
        yield action, n_times


def unroll_code(code: str) -> str:
    base_command = r'[FLR]\d*'
    composed = fr'\((?P<command>({base_command})+)\)(?P<repeat>\d*)'

    while True:
        prev_code = code
        code = re.sub(composed, unroll_command, prev_code)
        if code == prev_code:
            break
    return code


def unroll_command(match: Match) -> str:
    repeat = int(match['repeat']) if match['repeat'] else 1
    return match['command'] * repeat


def move_forward(position: Cell, direction: Direction, n_moves: int) -> List[Cell]:
    px, py = position
    dx, dy = direction.value
    return [(px + i * dx, py + i * dy) for i in range(1, n_moves + 1)]


def make_turn(start: Direction, side: str, n_turns: int) -> Direction:
    ordering = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
    step = 1 if side == 'R' else -1
    return ordering[(ordering.index(start) + step * n_turns) % len(ordering)]


def draw_path(visited_cells: Set[Cell]) -> str:
    max_x, min_x, max_y, min_y = find_cells_boundaries(visited_cells)

    rectangle = list()
    for y in range(max_y, min_y - 1, -1):
        row = ['*' if (x, y) in visited_cells else ' ' for x in range(min_x, max_x + 1)]
        rectangle.append(''.join(row))

    return '\r\n'.join(rectangle)


def find_cells_boundaries(visited_cells: Set[Cell]) -> Tuple[int, int, int, int]:
    max_x, _ = max(visited_cells, key=itemgetter(0))
    min_x, _ = min(visited_cells, key=itemgetter(0))

    _, max_y = max(visited_cells, key=itemgetter(1))
    _, min_y = min(visited_cells, key=itemgetter(1))
    return max_x, min_x, max_y, min_y

from typing import Tuple, Iterable, List

Position = Tuple[int, int]
Positions = List[Position]

MOVES: Tuple[Position, ...] = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))


def knights_tour(start: Position, size: int) -> Positions:
    board = [[False] * size for _ in range(size)]

    def moves(x: int, y: int) -> Iterable[Position]:
        for xd, yd in MOVES:
            xx, yy = x + xd, y + yd

            if 0 <= xx < size and 0 <= yy < size and not board[xx][yy]:
                yield xx, yy

    def dfs(path: Positions) -> Iterable[Positions]:
        if len(path) == size ** 2:
            yield path
            return

        x, y = path[-1]
        board[x][y] = True

        for vv in sorted(moves(x, y), key=lambda n: len([*moves(*n)])):
            path.append(vv)
            yield from dfs(path)
            path.pop()

        board[x][y] = False

    return next(dfs([start]), [])

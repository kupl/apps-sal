from random import shuffle
from typing import List
from concurrent.futures import ProcessPoolExecutor


def is_under_attack(queens: List[int], queen: int) -> bool:
    (x, y) = (queens.index(queen), queen)
    return any((x == xx or y == yy or abs(xx - x) == abs(yy - y) for (xx, yy) in enumerate(queens) if xx != x and yy != y))


def _nQueen(n: int) -> List[int]:
    if n in {2, 3}:
        return []
    queens = [*list(range(n))]
    shuffle(queens)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n):
            for j in range(i + 1, n):
                if is_under_attack(queens, queens[i]) or is_under_attack(queens, queens[j]):
                    (queens[i], queens[j]) = (queens[j], queens[i])
                    if is_under_attack(queens, queens[i]) and is_under_attack(queens, queens[j]):
                        (queens[i], queens[j]) = (queens[j], queens[i])
                    else:
                        swapped = True
    return queens


_solutions = []


def nQueen(n: int) -> List[int]:
    if not _solutions:
        with ProcessPoolExecutor() as pool:
            _solutions[:] = [*pool.map(_nQueen, list(range(51)))]
    return _solutions[n]

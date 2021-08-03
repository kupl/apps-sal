from typing import Dict, Generator, List, Tuple

K_MOVES = [
    (a, b)
    for a in [-2, -1, 1, 2]
    for b in [-2, -1, 1, 2]
    if abs(a) != abs(b)
]


def gen_k_moves(k: Tuple[int, int]) -> Generator[Tuple[int, int], None, None]:
    """
    Generates all valid knight moved from the given point
    """
    kc, kr = k
    for dc, dr in K_MOVES:
        c, r = kc + dc, kr + dr
        if 1 <= r <= 8 and 1 <= c <= 8:
            yield c, r


def solve(k: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    """
    Given the starting point of a knight k, return a dict of postions to minimum moves to that position
    """
    solutions = {}

    edges = [k]
    visited = set()
    steps = 0
    while edges:
        visited.update(edges)
        for edge in edges:
            solutions[edge] = steps
        steps += 1
        new_edges = []
        for edge in edges:
            for nk in gen_k_moves(edge):
                if nk in visited:
                    continue
                new_edges.append(nk)
                visited.add(nk)
        edges = new_edges
    return solutions


w1_solutions = solve((2, 1))
w2_solutions = solve((7, 1))
b1_solutions = solve((2, 8))
b2_solutions = solve((7, 8))


def whose_turn(positions):
    positions = [
        (ord(s[0]) - ord('a') + 1, int(s[1]))
        for s in positions.split(';')
    ]
    w1 = w1_solutions[positions[0]], w2_solutions[positions[0]]
    w2 = w1_solutions[positions[1]], w2_solutions[positions[1]]
    b1 = b1_solutions[positions[2]], b2_solutions[positions[2]]
    b2 = b1_solutions[positions[3]], b2_solutions[positions[3]]

    whites = min(w1[0] + w2[1], w1[1] + w2[0])
    blacks = min(b1[0] + b2[1], b1[1] + b2[0])
    return (whites % 2) == (blacks % 2)

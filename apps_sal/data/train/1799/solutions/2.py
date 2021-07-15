from random import choice, shuffle
from typing import List, Optional, Tuple

def decode(cr: str, size: int) -> Tuple[int, int]:
    """
    Decode chess notation into a row, col tuple
    E.g.: 'd2' -> (1, 3)
    """
    c = ord(cr[0]) - ord('a')
    r = (int(cr[1]) - 1) % size
    return r, c

def encode(r: int, c: int) -> str:
    """
    Encode a row, col tuple into chess notation (works up to a board size of 10)
    E.g.: (1, 3) -> 'd2'
    """
    return f'{chr(ord("a") + c)}{(r + 1) % 10}'

def build_coverage(queens: List[Tuple[int, int]], size: int) -> List[List[int]]:
    """
    Given the queens on a board of given size, returns a matrix of the coverage of
    each position on the board
    :param queens: List of queens with (row, column) coordinates
    :param size: Edge size of the board
    """
    result = [
        [0 for _ in range(size)] 
        for _ in range(size)
    ]
    for q, (qr, qc) in enumerate(queens):
        result[qr][qc] -= 2
        for i in range(size):
            result[i][qc] += 1
            result[qr][i] += 1
            if i == 0:
                continue
            for dr, dc in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                rr = qr + i * dr
                if 0 <= rr < size:
                    cc = qc + i * dc
                    if 0 <= cc < size:
                        result[rr][cc] += 1
    return result

def solve(queens: List[Tuple[int, int]], size: int) -> Optional[str]:
    """
    Given a list of (row, col) queen positions and a size of board, apply a iterative repair algorithm
    until we find a position where no queen can take another.
    :param queens: List of positions, the first queen will not be moved by the algorithm
    :param size: Size of the board
    :return: String containing chess encoded positions if a solution is found, None if too many cycles pass without a solution 
    """
    cycle = 0
    while True:
        cycle += 1
        coverage = build_coverage(queens, size)
        queen_coverage = [(coverage[qr][qc], qr, qc) for qr, qc in queens]
        
        if all(qc[0] == 0 for qc in queen_coverage):
            # Found solution
            break
        
        # Find most coverage on queens, and chose a random queen with that coverage
        most = max(qc[0] for qc in queen_coverage[1:])
        candidates = [
            (qr, qc, i) 
            for i, (c, qr, qc) in enumerate(queen_coverage[1:], 1) 
            if c == most
        ]
        # Target queen
        tr, tc, ti = choice(candidates)            

        # Find the positions with the lowest coverage on the same row
        best, best_pos = None, []
        for r in range(size):
            if r == tr:
                continue
            cov = coverage[r][tc]
            if best is None or cov < best:
                best, best_pos = cov, [r]
            elif cov == best:
                best_pos.append(r)
        
        # Move to a random row on the column (from options with the lowest coverage)
        queens[ti] = (choice(best_pos), tc)
        if cycle > 20:
            return None

    return ','.join([encode(qr, qc) for qr, qc in queens])

def queens(position, size):
    """
    Given a chess encoded queen position and a size of board, find and return a chess encoded series of positions where 
    no queen can take another.
    :param queen: Fixed position of one queen, e.g.: 'd5'
    :param size: Size of the board
    :return: String containing chess encoded positions of size queens that cannot take each other 
    """
    if size == 1:
        return 'a1'
    if size in [2, 3]:
        raise ValueError(f'No solution possible with size = {size}')

    fixed_r, fixed_c = decode(position, size)
    while True:
        # Build an initialrandomised state where no two queens share the same row or column
        rr = [i for i in range(size) if i != fixed_r]
        cc = [i for i in range(size) if i != fixed_c]
        shuffle(rr)
        shuffle(cc)
        queens = [(r, c) for r, c in zip([fixed_r] + rr, [fixed_c] + cc)]
        # Attempt to reduce conflicts until we find a solution
        result = solve(queens, size)
        if result:
            return result
        # Looks like we found a local optimum, so re-randomise and start again



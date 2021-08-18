from itertools import count

ALL_MOVES = [(1, 1), (0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
AMA_MOVES = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]


def amazon_check_mate(*args):

    def posInBoard(x, y): return 0 <= x < 8 and 0 <= y < 8

    def getCoveredPos(start, king=None):
        covered = {start}
        for m in (AMA_MOVES if king else ALL_MOVES):
            pos = tuple(z + dz for z, dz in zip(start, m))
            if posInBoard(*pos):
                covered.add(pos)

        if king:
            for dx, dy in ALL_MOVES:
                for n in count(1):
                    pos = (start[0] + dx * n, start[1] + dy * n)
                    if not posInBoard(*pos) or pos == king:
                        break
                    covered.add(pos)

        return covered

    K, Q = [(ord(s[0]) - 97, ord(s[1]) - 49) for s in args]
    kCover = getCoveredPos(K)
    fullCover = getCoveredPos(Q, K) | kCover
    freeQueen = Q not in kCover
    counts = [0] * 4

    for x in range(8):
        for y in range(8):
            black = (x, y)

            if black in kCover or black == Q:
                continue

            safePosAround = any(posInBoard(*neigh) and (neigh not in fullCover or neigh == Q and freeQueen)
                                for neigh in ((x + dx, y + dy) for dx, dy in ALL_MOVES))

            counts[2 * (black not in fullCover) + safePosAround] += 1

    return counts

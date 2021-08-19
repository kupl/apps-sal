from collections import defaultdict
MOVES = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)}


def find_word(board, word):
    dct = defaultdict(set)
    for (x, r) in enumerate(board):
        for (y, c) in enumerate(r):
            dct[c].add((x, y))
    paths = [[pos] for pos in dct[word[0]]]
    for c in word[1:]:
        if not paths or c not in dct:
            return False
        paths = [path[:] + [nextPos] for path in paths for nextPos in {pos for pos in dct[c] - set(path) if tuple((z2 - z1 for (z1, z2) in zip(pos, path[-1]))) in MOVES}]
    return bool(paths)

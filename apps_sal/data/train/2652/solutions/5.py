from itertools import combinations


def count_squares(lines):

    def is_valid(x, y, size):
        if any([chars.get((nx, y), '@') not in '-+' or chars.get((nx, y + size), '@') not in '-+' for nx in range(x + 1, x + size)]):
            return False
        if any([chars.get((x, ny), '@') not in '|+' or chars.get((x + size, ny), '@') not in '|+' for ny in range(y + 1, y + size)]):
            return False
        return True
    (chars, corners) = (dict(), [[] for _ in range(len(lines))])
    for (y, line) in enumerate(lines):
        for (x, ch) in enumerate(line):
            chars[x, y] = ch
            if ch == '+':
                corners[y].append(x)
    return sum((is_valid(tl, y, tr - tl) for (y, co) in enumerate(corners) for (tl, tr) in combinations(co, 2) if chars.get((tl, y + tr - tl)) == '+' and chars.get((tr, y + tr - tl)) == '+'))

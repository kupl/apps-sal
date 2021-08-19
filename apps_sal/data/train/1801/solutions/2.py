from collections import defaultdict


def interpreter(code, iterations, w, h):
    (cp, r, c, p, stk, brackets, grid) = (0, 0, 0, 0, [], {}, [[0] * w for _ in range(h)])
    for (i, cc) in enumerate(code):
        if cc == '[':
            stk.append(i)
        elif cc is ']':
            brackets[i] = stk.pop()
            brackets[brackets[i]] = i
    while p < iterations and cp < len(code):
        if code[cp] == '*':
            grid[r][c] = 0 if grid[r][c] else 1
        elif code[cp] == '[' and grid[r][c] == 0:
            cp = brackets[cp]
        elif code[cp] == ']' and grid[r][c] == 1:
            cp = brackets[cp]
        elif code[cp] == 'n':
            r = r - 1 if r else h - 1
        elif code[cp] == 'w':
            c = c - 1 if c else w - 1
        elif code[cp] == 's':
            r = r + 1 if r < h - 1 else 0
        elif code[cp] == 'e':
            c = c + 1 if c < w - 1 else 0
        (cp, p) = (cp + 1, p + 1 if code[cp] in '[]nsew*' else p)
    return '\r\n'.join([''.join((str(e) for e in r)) for r in grid])

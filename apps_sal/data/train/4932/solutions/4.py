def find_solution(puzzle):
    moves = set()
    n = len(puzzle)
    zeros = {(i, n + j) for (i, row) in enumerate(puzzle) for (j, v) in enumerate(row) if v == 0}
    if not zeros:
        return []

    def get():
        v = None
        if len(moves) == 0:
            return zeros.pop()
        for (r, c) in zeros:
            if r in moves or c in moves:
                if r in moves and c in moves:
                    continue
                v = (r, c)
                zeros.remove(v)
                return v
        if v is None:
            return zeros.pop()
    while zeros:
        (r, c) = get()
        if r not in moves:
            moves.add(r)
            for k in range(n, 2 * n):
                if k == c:
                    continue
                if (r, k) in zeros:
                    zeros.remove((r, k))
                else:
                    zeros.add((r, k))
        elif c not in moves:
            moves.add(c)
            for k in range(n):
                if k == r:
                    continue
                if (k, c) in zeros:
                    zeros.remove((k, c))
                else:
                    zeros.add((k, c))
    return list(moves)

def find_solution(m):
    return [n for (n, r) in enumerate(m) if r[0]] + [n for (n, c) in enumerate(m[0], len(m)) if not m[0][0] ^ c]
